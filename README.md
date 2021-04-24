# Building and packaging a Flask app for Production

## Structure:
- `flaskAppServer` dir - Contains the flask initialization and API server code.
- `tests` dir - Unit tests 

## Build
- make-image.sh

Builds the docker image which can be used in K8s or any stand alone deployment. 

## Makefile
- build: Builds the docker image.
- run: Runs the docker image.
- kill: Cleans up the docker container and image.

## Gunicorn
- Gunicorn is the python based WSGI HTTP Server to allow concurrency and load management in Production systems.

## Third-Party Libs
Name     | Version
---------|------------
Flask    | v1.1.2
Gunicorn | v20.0.4



  
 
