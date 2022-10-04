# Containerizing a microservice
# Containerization is a type of operating system virtualization in which applications are
# run in their separate user space, but sharing the same operating system. This separate
# user space is called a container. Docker is the most popular platform for creating,
# managing, and running applications as containers. Docker still holds more than an 80%
# market share, but there are other container runtimes such as CoreOS rkt, Mesos, lxc, and
# containerd. Before using Docker to containerize our microservice, we will quickly review
# the main components of the Docker platform:
# • Docker Engine: This is the core Docker application for building, packaging, and
# running container-based applications.
# • Docker image: A Docker image is a file that is used to run the application in a
# container environment. The applications developed using Docker Engine are stored
# as Docker images, which are a collection of application code, libraries, resource files,
# and any other dependencies that are required for application execution.
# • Docker Hub: This is an online repository of Docker images for sharing within your
# team and with the community as well. Docker Registry is another term used in the
# same context. Docker Hub is an official name of the Docker registry that manages
# Docker image repositories.
# • Docker Compose: This is a tool for building and running container applications
# using a YAML-based file instead of using the CLI commands of Docker Engine.
# Docker Compose provides an easy way to deploy and run multiple containers with
# configuration attributes and dependencies. Therefore, we will recommend using
# Docker Compose or similar technology to build and run your containers.
# To use Docker Engine and Docker Compose, you need to have an account with the
# Docker registry. Also, you must download and install Docker Engine and Docker
# Compose on your machine before starting the following steps:
# 1. As a first step, we will create a list of our project dependencies by using the pip
# freeze command file as follows:
# pip freeze -> requirements.txt
# This command will create a list of dependencies and export them to the
# requirements.txt file. This file will be used by Docker Engine to download
# these libraries inside the container on top of a Python interpreter. The contents of
# this file in our project are as follows:
# asgiref==3.4.1
# Django==3.2.5408
# Using Python for Microservices Development
# django-rest-framework==0.1.0
# djangorestframework==3.12.4
# pytz==2021.1
# sqlparse==0.4.1
# 2. In the next step, we will build Dockerfile. This file will also be used by Docker
# Engine to create a new image of a container. In our case, we will add the following
# lines to this file:
# FROM python:3.8-slim
# ENV PYTHONUNBUFFERED 1
# WORKDIR /app
# COPY requirements.txt /app/requirements.txt
# RUN pip install -r requirements.txt
# COPY . /app
# CMD python manage.py runserver 0.0.0.0:8000
# The first line in this file is setting the base image for this container, and we set it
# to Python:3.8-slim, which is already available in the Docker repository. The
# second line in the file is setting an environment variable for better logging. The rest
# of the lines are self-explanatory as they are mostly Unix commands.
# 3. As a next step, we will create a Docker Compose file (docker-compose.yml) as
# follows:
# version: '3.7'
# services:
# gradesms:
# build:
# context: .
# dockerfile: Dockerfile
# ports:
# - 8000:8000
# volumes:
# - .:/appBuilding microservices-based applications
# 409
# This is a YAML file, and we define containers as services in it. Since we have only
# one container, we defined the gradesms service. Note that build is pointing
# to Dockerfile we just created and assuming it is in the same directory as this
# docker-compose.yml file. The container port 8000 is mapped to the web server
# port 8000. This is an important step in allowing traffic from the container to your
# application inside the container.
# 4. As the last step, we mount the current directory (.) to the /app directory inside
# the container. This will allow the changes made on our system to be reflected in the
# container and vice versa. This step is important if you are creating containers during
# the development cycle.
# 5. We can start our container by using the following Docker Compose command:
# docker-compose up
# For the first time, it will build a new container image and will require internet access
# to download the base container image from the Docker registry. After creating a
# container image, it will automatically start the container.
# Details of how Docker Engine and Docker Compose work are beyond the scope of this
# book, but we recommend that you become familiar with container technology such as
# Docker through their online documentation (https://docs.docker.com/).