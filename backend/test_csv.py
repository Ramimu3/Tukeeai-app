import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AIDTdjango.settings')
django.setup()

from myapp.tasks import process_file_to_csv

crew_ai_output = "/home/rami/Documents/GitHub/AIDT2/backend/media/chunks/ramimum/45/user_2_crew_ai_outputs"
user_id = "user_2"

result = process_file_to_csv(crew_ai_output, user_id)
print("Result:", result)
