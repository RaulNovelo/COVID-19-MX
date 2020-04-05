# COVID-19-MX 🦠 📈

Dashboard to show the last Coronavirus data in _México_. This repository contains the process of data mining from official sources, cleaning the data and store it in a Relational Database to finally show it in a human-readable way.

![](https://overflow.ai/static/tracker/images/coronavirus_dashboard_mexico.png)

## Requirements

This project is built with Django 3.0 and uses the following libraries:

- `beautifulsoup4`: Library for extract PDF links from Government website.
- `camelot-py`: **Super** powerful tool to parse PDF to CSV.
- `pandas`: Auxilary library to handle CSV in an easy way.
- `requests`: Library to make HTTP requests.

All the libraries are found in the `requirements.txt` file and can be install using the command `pip install -r requirements.txt`. It's recommended to use a Virtual Environment when installing new libraries.

## Data source

Data extracted from [Mexican Government Daily Technical Report](https://www.gob.mx/salud/documentos/nuevo-coronavirus-2019-ncov-comunicado-tecnico-diario?idiom=es).

##### Data processing

All the data mining is found in the file
`scripts/fetch_data.py`. It contains all the functions to web scrap, download, parse and store in Sqlite3.

It can be run using Django Extensions:

```
python3 manage.py runscript fetch_data -v2
```

## Frontend

The frontend relies in lightweight and open sources libraries:

- [Openlayers](https://github.com/openlayers/openlayers): Library to manage all related with the map. Rendering, clustering, gestures, etc.
- [Fluidable](https://fluidable.com/): Simple and lightweight grid system. Bootstrap is simply too much for this project.
- [Apexcharts.js](https://github.com/apexcharts/apexcharts.js): Amazing charts thanks to them.


## Configuración

## Requisitos
- Tener instalado GIT.
- Python versión 3.6,>.
- Un entorno virtual listo para usar.

### Instalación

Al descargar el proyecto encontraremos un archivo llamado "requirements.txt" el cual contiene todas las dependencias Python para ejecutar el proyecto. 

Ejecutamos lo siguiente: 

    $ pip install -r requirements.txt

### Ejecución del proyecto
Para correr el servidor de scrapy y poder consumir los spiders, ejecutamos:

    $ python manage.py runserver

En otra terminal tenemos que activar el entorno virtual para correr

### Contenedores
Se proporciona el archivo `Dockerfile` y `docker-compose.yml` para ejecución del servicio desde contenedores de Docker.

`web`: servidor de django con integracion de socket.io

`worker`: servicio de celery para ejecutar tareas programadas

#### Ejecución

    $ docker-compose up

# Powered by Open Source Projects. 

Agradecemos enormemente el esfuerzo de las comunidades que mantienen el desarrollo de los siguientes proyectos.

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Python SocketIO](https://python-socketio.readthedocs.io/en/latest/)
- [Celery](http://www.celeryproject.org/)
- [Gunicorn](https://gunicorn.org/)
- [RabbitMQ](https://www.rabbitmq.com/)

# Despligue en Heroku
Para el despligue en la plataforma [Heroku]() se proporciona un archivo llamado `Procfile` con el comando de automatización de despligue del proyecto. Los comandos para cada servicio son los correspondientes para ejecutar en producción.

`Procfile`
```
web: gunicorn -k eventlet -w 1 --threads=5 apigateway.wsgi:application --log-level=debug
worker: celery worker -A apigateway -B --loglevel=INFO
```
`web`: servidor de django con integracion de socket.io

`worker`: servicio de celery para ejecutar tareas programadas

Make with love by [@RaulNovelo](https://github.com/RaulNovelo).
