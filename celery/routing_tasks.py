from celery import Celery
import time


app = Celery('tasks', broker='redis://localhost:6379/14', backend='redis://localhost:6379/15')

# The simplest way to do routing is to use the task_create_missing_queues setting.
# By default it is set to True.
# for manual routing, please check the user guide
# https://docs.celeryproject.org/en/stable/userguide/routing.html#manual-routing

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Asia/Dhaka',
    enable_utc=True,
)

# The task_routes setting can either be a dictionary, or a list of router objects,
# so in this case we need to specify the setting as a tuple containing a list.
# details : https://docs.celeryproject.org/en/stable/userguide/routing.html

# dictionary
app.conf.task_routes={
    'routing_tasks.short_task': {'queue': 'short_queue'},
    'routing_tasks.long_task': {'queue': 'long_queue'}
}

## list of router objects
# app.conf.task_routes = ([
#     ('routing_tasks.short_task', {'queue': 'short_queue'}),
#     ('routing_tasks.long_task', {'queue': 'long_queue'}),
# ],)

# After the setup above:
# - long tasks will go to queue named 'long'
# - short tasks will go to queue named 'short'
# - other tasks will go to default queue (named 'celery')

# We can also specify the queue at runtime with the queue argument to apply_async. 
# i.e.,: 
# >>> from proj.tasks import add
# >>> add.apply_async((2, 2), queue='hipri')
# src : https://docs.celeryproject.org/en/stable/getting-started/next-steps.html#routing


@app.task
def long_task():
    time.sleep(10)
    return "Long task completed"


@app.task
def short_task():
    time.sleep(1)
    return "Short task completed"


@app.task
def medium_task():
    time.sleep(5)
    return "Medium task completed"
