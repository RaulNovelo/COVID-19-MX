# ===================================================
# Celery Task/Schedulers
# ===================================================

# celery imports
from celery.decorators import task
from celery.task.schedules import crontab
from celery.decorators import periodic_task

# project imports
from .models import *
from project.scrapy_api import scrapyd
from .fetch_data import generate

# ===================================================
# Tasks
# ===================================================

@periodic_task(run_every=(crontab(minute=0, hour='*/2')), name="update_info: Scrap https://www.gob.mx/ website every 2 hrs")
def update_info():
    """
    This is a real world task.
    """
    print("Updating data...")
    generate()
        

