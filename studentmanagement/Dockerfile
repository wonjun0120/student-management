FROM python:3

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# CMD ["python3", "run.py"]
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]
