# FASTAPI (TEST)
FROM python:3.13.1-bookworm     

WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt --upgrade pip

EXPOSE 8000

COPY ./app /code/app


# CMD ["fastapi", "run", "app/main.py", "--port", "80"] # BIEN!

# CMD ["uvicorn", "app.main:app", "--port", "80"] 
CMD ["uvicorn", "app.main:app", "--port", "8000", "--host", "0.0.0.0"]