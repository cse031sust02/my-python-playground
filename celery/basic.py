from tasks import some_task

result = some_task.delay(100000000)
print('task was called')

# Result Backend
print("Is Result Ready? : ",result.ready())
print("AsyncResult instance : ",result)
print("Returned Value : ",result.get())
print("Is Result Ready? : ",result.ready())