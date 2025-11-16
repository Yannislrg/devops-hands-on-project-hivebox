FROM python:3.13

WORKDIR /HIVEBOX

COPY src/ /HIVEBOX/

COPY requirements.txt /HIVEBOX/

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "fastapi", "run", "main.py" ]