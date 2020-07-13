from celery import Celery

app = Celery(broker='redis://localhost:6379/14', backend='redis://localhost:6379/15')

@app.task
def some_task(n):
     result = 0
     for i in range(n):
          result += i
     return result