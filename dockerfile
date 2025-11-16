FROM python:3.13

WORKDIR /HIVEBOX

COPY src/ /HIVEBOX/

CMD [ "python", "main.py" ]