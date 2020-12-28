from celery import Celery
from time import sleep

# The first argument to Celery is the name of the current module. This is only
# needed so that names can be automatically generated when the tasks are
# defined in the __main__ module.
app = Celery('tasks', broker='redis://localhost:6379/14', backend='redis://localhost:6379/15')

# The default configuration should be good enough for most use cases, but
# there are many options that can be configured to make Celery work exactly
# as needed.
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Asia/Dhaka',
    enable_utc=True,
)

@app.task
def demo_task(n):
     result = 0
     for i in range(n):
          result += i
     return result

