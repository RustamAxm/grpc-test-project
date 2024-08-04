FROM python:3.10.11

WORKDIR /app
RUN python -m pip install grpcio grpcio-tools
COPY . /app
RUN ./generate.sh
ENTRYPOINT ["python", "/app/greeter_server.py"]
