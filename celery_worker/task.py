
# celery_worker/tasks.py
from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672/whatsapp')

@app.task
def process_message(message):
    print("Processing message:", message)
    # Implement message processing logic here
    # This can include parsing, validation, transformation, etc.
