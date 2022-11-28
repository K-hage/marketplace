FROM python:3.10

WORKDIR /app/skymarket/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY poetry.lock pyproject.toml /app/
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install -n --no-ansi
COPY .env /app/skymarket/
COPY ./skymarket/ ./

CMD python manage.py runserver 0.0.0.0:8000
