# ===================================================
# Celery Task/Schedulers
# ===================================================

# project imports
from .models import *
from project.scrapy_api import scrapyd

# celery imports
from celery.decorators import task
from celery.task.schedules import crontab
from celery.decorators import periodic_task

# ===================================================
# Tasks
# ===================================================

# decorador scheduler
@periodic_task(run_every=(crontab()), name="my_periodic", ignore_result=False)
def my_periodic():
    pass


@task(name="my_task")
def my_task():
    pass
        
        

