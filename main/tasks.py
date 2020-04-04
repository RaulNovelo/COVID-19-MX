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
from .scripts.fetch_data import run

# ===================================================
# Tasks
# ===================================================

@periodic_task(run_every=(crontab()), name="update_info: Scrap https://www.gob.mx/ website every 2 hrs")
def update_info():
    """
    This is a real world task.
    """
    print("Updating data...")
    run()
        

