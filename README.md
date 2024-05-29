# Fastapi-template
A python project template with fastapi. This template is intented for Rich type projects, but you can easily adapt it for more CRUD type projects.

I use a basic task api as an example.

# Project setup

## Initialize project with poetry
```bash
poetry new fastapi-template
```

You can then create the repository and push the code.

## Install dependencies
```bash
poetry add a-dependency
```

## Add dev dependencies
A dev dependency is a dependency that is only needed for development and not for production.
```bash
poetry add --dev a-dev-dependency
```

## Add a script
You can add a script to the pyproject.toml file.
```toml
[tool.poetry.scripts]
my-script = "my_module:my_function"
```

## Run the project
You can either run the project with poetry or with the make file.
```bash
poetry run uvicorn app.main:app --reload
```
or
```bash
make run
```
