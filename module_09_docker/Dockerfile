FROM python:3.7.9-slim-stretch

RUN mkdir /app

COPY requirements.txt /app/

RUN python -m pip install -r /app/requirements.txt

COPY my_app.py /app/

WORKDIR /app

ENTRYPOINT ["python3", "my_app.py"]