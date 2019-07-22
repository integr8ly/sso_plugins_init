FROM python:3

COPY keycloak-metrics-spi.jar ./
COPY openshift4-idp.jar ./

COPY themes/ ./themes/

COPY plugins.py ./

CMD [ "python", "./plugins.py"]

