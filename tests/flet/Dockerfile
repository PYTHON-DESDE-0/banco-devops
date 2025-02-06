# FLET (TEST)

ARG VERSION=3.13.1-slim-bookworm 
FROM python:${VERSION}     
# FROM python:3.13.1-bookworm     

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt --upgrade pip

COPY ./src /code/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--port", "8000", "--host", "0.0.0.0"]
