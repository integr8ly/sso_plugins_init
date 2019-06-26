FROM python:3-alpine

COPY keycloak-metrics-spi.jar ./
COPY plugins.py ./

CMD [ "python", "./plugins.py"]

