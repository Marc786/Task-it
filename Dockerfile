FROM python:3.12

RUN pip3 install poetry

COPY pyproject.toml poetry.lock ./
COPY . .

EXPOSE 8080

RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "-m", "main", "--env", "prod"]
