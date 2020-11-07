# FROM ubuntu:16.04

# RUN apt-get update -y && \
#     apt-get install -y python-pip python3

# # We copy just the requirements.txt first to leverage Docker cache
# COPY ./requirements.txt /app/requirements.txt

# WORKDIR /app

# # RUN pip3 install --upgrade pip3

# RUN pip3 install -r requirements.txt

# COPY . /app

# CMD ["python3","app.py"]

# ENTRYPOINT [ "python" ]

# CMD [ "app.py" ]

FROM python:alpine3.7 
# FROM python:3.6.1-alpine
WORKDIR /app
COPY . /app
RUN python -m pip install --upgrade setuptools pip wheel
RUN pip install -r requirements.txt
CMD ["python","app.py"]