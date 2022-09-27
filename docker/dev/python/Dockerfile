FROM python:3.10

COPY ./requirements /requirements

RUN apt-get update && apt-get -y install gettext && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r /requirements/dev.txt && rm -rf /requirements

WORKDIR /app

COPY ./app /app

COPY ./docker/dev/python/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["bash","/entrypoint.sh"]
