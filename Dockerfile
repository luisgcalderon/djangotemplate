# pull official base image
FROM python:3.8

# accept arguments
ARG PIP_REQUIREMENTS=dev.txt

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip setuptools

#

# create
RUN yum -y update & yum clean all
