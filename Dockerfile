FROM python:3.10.11

WORKDIR /app
COPY . /app
ENV PYTHONPATH=/app
RUN python -m pip install -r requirements.txt
RUN ./generate.sh
ENTRYPOINT ["python", "/app/grpc_test_project/greeter_server.py"]
