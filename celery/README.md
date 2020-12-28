## Flow
- install celery
- define Celery application/app
  - configure broker, backend etc
- define tasks
- running the worker

### Running the Celery worker server
```
$ celery -A tasks worker --loglevel=INFO
```

- Help
```
 celery worker --help
```

```
IMPORTANT NOTES FROM HELP
===========================

Start worker instance.

Examples -------- 
$ celery --app=proj worker -l INFO 
$ celery -A proj worker -l INFO -Q hipri,lopri
$ celery -A proj worker --concurrency=4 
$ celery -A proj worker --concurrency=1000 -P eventlet $ celery worker --autoscale=10,0

Worker Options:
  -n, --hostname                  Set custom hostname (e.g., 'w1@%%h').
                                 
  -l, --loglevel                  Logging level [DEBUG|INFO|WARNING|ERROR|CRITICAL|FATAL]


Pool Options:
  -c, --concurrency               Number of child processes processing the
                                  queue.  The default is the number of CPUs
                                  availableon your system.

  -P, --pool                      Pool implementation. [prefork|eventlet|gevent|solo]
  
  -E, --task-events, --events     Send task-related events that can be
                                  captured by monitors like celery events,
                                  celerymon, and others.




Embedded Beat Options:
  -B, --beat
```

---

## Demo 1 : Basics

- run the worker
```
$ celery -A basic_tasks worker -l INFO
```

- run the demo
```
$ python basic_demo.py
```

---

## Demo 2 : Routing Tasks

- run the worker which will consume the long_tasks by subscribing long_queue
```
$ celery -A routing_tasks worker -n long_worker -Q long_queue -l INFO
```

> note : 
if we set task_create_missing_queues=False, it will show the following error for the above commands
```
...
celery.exceptions.ImproperlyConfigured: Trying to select queue subset of ['long_queue'], but queue 'long_queue' isn't
defined in the `task_queues` setting.

If you want to automatically declare unknown queues you can
enable the `task_create_missing_queues` setting.
```

- run the worker which will consume the short tasks by subscribing short_queue
```
$ celery -A routing_tasks worker -n short_worker -Q short_queue -l INFO
```

- run the default worker
```
$ celery -A routing_tasks worker -n default -l INFO
```

- run the demo
```
$ python routing_demo.py
```

---

## Demo 3 : Workflow

- run the worker
```
$ celery -A workflow_tasks worker -l INFO
```

- run the demo
```
$ python workflow_demo.py
```
