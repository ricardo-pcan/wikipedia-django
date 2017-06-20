# wikipedia-django
Django Rest Project for wikipedia download pdf

## Requeriments
* Docker
* Docker Compose
* Fabric
* VO Fabutils

## Up and running
This project uses docker container. The containers flow and configurations are in `docker-compose.yml`.
Once installed the requeriments you only have to run `docker-compose up` for run the containers.
The services by default are:
* Python (Django) : Port 8000

This microservice get the pdf from Wikipedia Id, for get the pdf exists the endpoint `api/v1/wikipedias/get-pdf`.
For get pdf you have to pass the query param `title` with the wikipedia id value
