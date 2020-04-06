FROM python:3.6.6  

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /
COPY requirements.txt ./  
RUN apt-get install libsm6 libxrender1 libfontconfig1 libice6
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt  
RUN rm requirements.txt  

COPY . /  
WORKDIR /app