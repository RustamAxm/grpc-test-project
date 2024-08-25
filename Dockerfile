FROM python:3.10.11

WORKDIR /app
COPY . /app
RUN python -m pip install -r requirements.txt
RUN ./generate.sh
ENTRYPOINT ["python", "/app/greeter_server.py"]
