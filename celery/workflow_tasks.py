from celery import Celery
from time import sleep


app = Celery('tasks', broker='redis://localhost:6379/14', backend='redis://localhost:6379/15')
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Asia/Dhaka',
    enable_utc=True,
)


@app.task
def add(i, j):
     sum = i + j
     return sum


@app.task
def chain_part_1(first_name, last_name):
     sleep(3)
     return "{} {}".format(first_name, last_name)


@app.task
def chain_part_2(fullname):
     sleep(2)
     return "Hello, {}!".format(fullname)