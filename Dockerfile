FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
# 加入下面這行安裝 netcat
RUN apt-get update && apt-get install -y netcat-traditional
COPY . /app/