FROM python:3

COPY keycloak-metrics-spi.jar ./
COPY plugins.py ./

CMD [ "python", "./plugins.py"]

