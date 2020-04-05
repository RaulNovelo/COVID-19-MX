# ===================================================
# Celery Task/Schedulers
# ===================================================

# celery imports
from celery.decorators import task
from celery.task.schedules import crontab
from celery.decorators import periodic_task

# project imports
from .models import DailyReport, Country
from project.scrapy_api import scrapyd
from .fetch_data import generate
import requests
import json
import os

# ===================================================
# Tasks
# ===================================================

# @periodic_task(run_every=(crontab(minute=0, hour='*/2')), name="update_info: Scrap https://www.gob.mx/ website every 2 hrs")
# def update_info():
#     """
#     This is a real world task.
#     """
#     print("Updating data...")
#     generate()
        

# crontab(minute=0, hour='*/6')
@periodic_task(run_every=(crontab()), name="update_info: GET https://pomber.github.io/covid19/timeseries.json every 12 hrs")
def update_reports():
    url = "https://pomber.github.io/covid19/timeseries.json"
    r = requests.get(url)
    data = r.json()
    api_key = os.environ.get('GEOAPIKEY', None)
    for country_name in data:
        last_report = data[country_name][-1]
        country = country_name

        # Get Country from DB. If not possible then create a new register
        try:
            country = Country.objects.get(name=country_name)
        except:
            url = f'https://api.opencagedata.com/geocode/v1/json?q={country_name}&key={api_key}&no_annotations=1'
            r = requests.get(url)
            geo_result = r.json()
            geo_result = geo_result['results'][0]['geometry']
            print(geo_result)
            country = Country(
                name=country_name, latitude=geo_result['lat'], longitude=geo_result['lng'])
            country.save()

        # Get Report from DB. If not possible then create a new register
        try:
            report = DailyReport.objects.get(country=country)
            report.date=last_report['date']
            report.confirmed=last_report['confirmed']
            report.deaths=last_report['deaths']
            report.recovered = last_report['recovered']
        except:
            report = DailyReport(
                country=country,
                date=last_report['date'],
                confirmed=last_report['confirmed'],
                deaths=last_report['deaths'],
                recovered=last_report['recovered']
            )
        finally:
            report.save()
            print(report)


        