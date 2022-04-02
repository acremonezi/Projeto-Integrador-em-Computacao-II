FROM python:3.9

RUN pip install --upgrade pip

COPY ./django_project/requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p /app

WORKDIR /app

COPY ./devops/django_gunicorn/entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]