# local development


## Table of contents
- [Prerequisites](#prerequisites)
- [Introduction](#introduction)
- [Setup Python environment](#setup-python-environment)
- [Setup Application](#setup-application)
  - [api](#api)
  - [postgres-db](#postgres-db)
- [Build the Application from docker-compose file](#build-the-application-from-docker-compose-file)
- [Create containers based on docker-compose file](#create-containers-based-on-docker-compose-file)


## Prerequisites

* Docker desktop installed ([source](https://www.docker.com/products/docker-desktop/))
* Python 3.11 installed ([source](https://www.python.org/downloads/release/python-3110/))


## Introduction

Local Development is split in two:

1. Local Environment
2. Local Application

In order to develop locally need a Python environment correctly setup and an instance of the Application running are required. Docker will be used to run the Application.

Both the Application image and the local Python environment share/use the packages listed in the [/server/requirements.txt](../server/requirements.txt) file. The Application needs it to run, and we need it in the local Python environment in order to develop locally (import packages, be able to debug, etc.). This is key for local development.


## Setup Python environment

0. Make sure you are inside the root of the project (`/py-fastapi`)

1. create virtual environment using venv
   * run `py -3.11 -m venv venv`
      * this will create a fresh Python environment using `Python 3.11` with the name `venv`

2. activate the virtual environment
   * run `/venv/Scripts/activate.bat`

3. install dependencies
   * run `pip install -r /server/requirements.txt`
     * this will install all Python packages listed in the `/server/requirements.txt` file inside the new `venv` environment

After all that you should have a fresh Python 3.11 environment setup.

You can check the environment by running `py --list`, you should see something like `*  Active venv` - The `*` means this is the current environment and `venv` is the name.

You can check the Python packages installed in this environment by running `pip freeze`.


## Setup Application

The Application is split in two services (`api` and `postgres-db`) and those services are defined in [/.docker/docker-compose.yaml](../.docker/docker-compose.yaml) file.

### api
The `api` service is the FastAPI application. This service is built from the [/.docker/app.dockerfile](../.docker/app.dockerfile) file.

### postgres-db
The `postgres-db` service is the application database. This service is built from a postgres:15-alpine image.

## Build the Application from docker-compose file
* checkout to `.docker` dir
  * run `cd .docker`
* build the image
  * run `docker compose build`

## Create containers based on docker-compose file
* run `docker compose up -d`
  * this will start our Application containers
