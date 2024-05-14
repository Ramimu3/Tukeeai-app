from celery import shared_task
import pandas as pd
import os
from django.conf import settings
from django.contrib.auth.models import User  # Import the User model
from myapp.models import UploadedFile
from celery_progress.backend import ProgressRecorder
from celery import Celery
import time
from datetime import datetime
from celery import Task
from .models import TaskResult
from django.utils import timezone
from .processing import convert_and_split, run_crew_ai, process_folder_to_single_csv


app = Celery('tasks', backend='rpc://', broker='amqp://username:password@localhost:5672//')


from celery import shared_task
from celery_progress.backend import ProgressRecorder
from .models import TaskResult

@shared_task(bind=True)
def process_file(self, file_id, user_id=None):
    progress_recorder = ProgressRecorder(self)

    task_result = TaskResult.objects.create(
        task_id=self.request.id,
        user_id=user_id,
        status='PROGRESS',
        progress=0
    )

    try:
        # Update progress at the beginning of the task
        progress_recorder.set_progress(0, 100, description='Starting file processing...')

        # Step 1: Convert and split the file
        output_dir = convert_and_split(file_id, user_id)
        progress_recorder.set_progress(30, 100, description='File conversion and splitting completed.')

        # Step 2: Run Crew AI on the chunks
        chunks_path = output_dir
        results = run_crew_ai(chunks_path, user_id)
        progress_recorder.set_progress(60, 100, description='Crew AI processing completed.')

        # Step 3: Process the Crew AI output to CSV
        crew_ai_output = results
        output_csv_filename = f"{user_id}_output.csv" if user_id else "output.csv"
        timestamp = timezone.now().strftime("%Y%m%d_%H%M%S")
        output_csv_filename = f"{user_id}_output_{timestamp}.csv" if user_id else f"output_{timestamp}.csv"
        output_csv_path = os.path.join(settings.MEDIA_ROOT, 'processed_csv', output_csv_filename)
        os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
        process_folder_to_single_csv(crew_ai_output, output_csv_path)
        progress_recorder.set_progress(90, 100, description='CSV processing completed.')

        # Update task status and output file path in the database
        task_result.status = 'SUCCESS'
        task_result.progress = 100
        task_result.output_file = os.path.join('processed_csv', output_csv_filename)
        task_result.save()

        # Return the result
        return {'message': 'File processing completed successfully.', 'output_file': os.path.join('processed_csv', output_csv_filename)}
    except Exception as e:
        # Update task status in case of failure
        task_result.status = 'FAILURE'
        task_result.save()
        return str(e)
