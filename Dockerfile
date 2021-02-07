FROM python:3.8
RUN mkdir /app
WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml /app/

# to prevent poetry from installing the actual app,
# and keep docker able to cache layers
RUN mkdir -p /app/src/app
RUN touch /app/src/app/__init__.py

RUN poetry install -n

# now actually copy the real contents of my app
COPY . /app

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
