FROM test_app

RUN mkdir /app

COPY requirements.txt /app/

RUN python -m pip install -r /app/requirements.txt

COPY my_app.py /app/

WORKDIR /app

ENTRYPOINT ["python", "my_app.py"]