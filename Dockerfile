FROM python:3.10.9-alpine3.17

RUN apt-get update -y
RUN python-pip

# Install required libraries
RUN pip install -r requirements.txt
RUN pip install -e .
