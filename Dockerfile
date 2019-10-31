FROM python:3-alpine

COPY themes/ ./themes/

COPY plugins.py ./

CMD [ "python", "./plugins.py"]

