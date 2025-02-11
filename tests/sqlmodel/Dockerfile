# SQLMODEL (TEST)

ARG PUERTO_POSTGRES='5432'
ENV PUERTO_POSTGRES=${PUERTO_POSTGRES}
ARG USUARIO_POSTGRES='postgres'
ENV USUARIO_POSTGRES=${USUARIO_POSTGRES}
ARG PASSW_POSTGRES='123456'
ENV PASSW_POSTGRES=${PASSW_POSTGRES}
ARG DATABASE_POSTGRES='test-db'
ENV DATABASE_POSTGRES=${DATABASE_POSTGRES}

ARG VERSION=3.13.1-slim-bookworm 
FROM python:${VERSION}     
# FROM python:3.13.1-bookworm     

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt --upgrade pip

COPY ./src /code/app

# EXPOSE 8000

# CMD ["python", "./app/main.py"]
CMD ["python", "app/main.py"]
# CMD ["py", "app/main.py"]
# CMD ["py", "./app/main.py"]

# CMD ["uvicorn", "app.main:app", "--port", "8000", "--host", "0.0.0.0"]
