FROM python:3.10


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app


# CMD ["uvicorn", "app.main:app", "--reload", "--port", "8000"]

CMD ["hypercorn", "app.main:app", "--bind", "::"]
