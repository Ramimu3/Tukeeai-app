FROM python:3.12
WORKDIR /backend

RUN pip install --upgrade pip

COPY panda-wheel /panda-wheel

RUN pip install --no-index --find-links=/panda-wheel pandas

COPY requirements.txt .

# Install dependencies using both the pre-built wheels and PyPI as fallback
RUN pip install --find-links=/panda-wheel -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
