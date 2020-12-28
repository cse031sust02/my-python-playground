from routing_tasks import short_task, long_task, medium_task

long_task.delay()
print('long task was called')

medium_task.delay()
print('medium task was called')

short_task.delay()
print('short task was called')
