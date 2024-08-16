.PHONY: run-prod
run-prod:
	@ poetry run python main.py --prod --logging json

.PHONY: run-dev
run-dev:
	@ poetry run python main.py --dev --logging pretty

.PHONY: tests
tests:
	@ poetry run pytest .

.PHONY: coverage
coverage:
	@ poetry run pytest --cov=task_it --cov-report=html:tests-reports/coverage

.PHONY: black
black:
	@ poetry run black .

.PHONY: ruff
ruff:
	@ poetry run ruff check . --fix

.PHONY: codeChecks
codeChecks:
	@ make ruff && make black

.PHONY: pyright
pyright:
	@ poetry run pyright .
	