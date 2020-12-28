from basic_tasks import demo_task

# Executing a task is done with apply_async(), or its shortcut: delay().
# While delay is convenient, it doesn’t give us as much control as using apply_async.
# With apply_async we can override the execution options. In addition we can set
# countdown/eta, task expiry, provide a custom broker connection and more.
result = demo_task.delay(100000000)
print('task was called')

# Calling a task returns an AsyncResult instance. This can be used to check the
# state of the task, wait for the task to finish, or get its return value (or if
# the task failed, to get the exception and traceback)
print("Result (AsyncResult instance) : ", result)
print("Is Result Ready? : ", result.ready())
print("Returned Value : ", result.get())
print("Is Result Ready? : ", result.ready())
