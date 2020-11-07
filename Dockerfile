FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python","app.py"]

# ENTRYPOINT [ "python" ]

# CMD [ "app.py" ]

# FROM python:3.6.1-alpine
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# CMD ["python","app.py"]