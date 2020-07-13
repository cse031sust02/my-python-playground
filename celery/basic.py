from tasks import some_task

result = some_task.delay(100000000)
print('celery called')

# Result Backend
print("Is Result Ready? : ",result.ready())
print("Result : ",result.get())
print("Is Result Ready? : ",result.ready())