FROM python:3.10-slim-buster
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /var/log/mushelfbackend
RUN apt-get update -y && \
    apt-get install -y default-libmysqlclient-dev python-dev build-essential pkg-config && \
    apt-get install -y libmariadb-dev-compat libmariadb-dev
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
ENTRYPOINT sh entrypoint.sh