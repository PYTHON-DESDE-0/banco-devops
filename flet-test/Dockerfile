FROM python:3.13.1-bookworm     

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt --upgrade pip

COPY ./src /code/src


CMD ["flet", "run", "src/main.py","--web", "--port", "8000"]
