FROM python:3.13.1-bookworm     

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt --upgrade pip

COPY ./src /code/src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--port", "8000", "--host", "0.0.0.0"]

