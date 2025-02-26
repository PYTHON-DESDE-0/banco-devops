# SQLMODEL (TEST)

ARG VERSION=3.13.1-slim-bookworm 
FROM python:${VERSION}     

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt --upgrade pip

COPY ./src /code/app

# EXPOSE 8000


CMD ["python", "app/main.py"]
