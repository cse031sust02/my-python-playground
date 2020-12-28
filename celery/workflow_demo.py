from celery import group, chain
from workflow_tasks import add, chain_part_1, chain_part_2

# Experiment with Canvas: Designing Work-flows
# https://docs.celeryproject.org/en/stable/getting-started/next-steps.html#canvas-designing-work-flows

# GROUP
# ========
# A group is used to call a list of tasks in parallel, and it returns a special result
# instance that lets you inspect the results as a group, and retrieve the
# return values in order.
job = group([
    add.s(2, 2),
    chain_part_1.s('Talha', 'Imam'),
    add.s(8, 8),
    add.s(16, 16),
    add.s(32, 32),
    chain_part_2.s("Talha Ibne Imam")
])
result = job.delay()
print(result.get())  # it is blocking when we are using get()
# output : [4, 'Talha Imam', 16, 32, 64, 'Hello Talha Ibne Imam']


# CHAIN 
# =========
# Tasks can be linked together so that one task is called after one task returns
# In the example below first task is return full name from the first name and last name
# and second task is greeting that fullname.
# Note that, we do not need to pass the output of the first tast to second task
chain(chain_part_1.s('Talha', 'Imam') | chain_part_2.s()).delay()


# CHUNK
# =======
items = zip(range(1000), range(1000))  # 1000 items
print(items)
add.chunks(items, 10).delay()