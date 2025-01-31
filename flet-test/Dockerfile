FROM python:3.13.1-bookworm     

WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt --upgrade pip


COPY ./app /code/app


CMD ["fastapi", "run", "app/main.py", "--port", "80"]