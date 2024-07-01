# Sensemitter QA Automation Tech Assignment by Ivan Erofeev

**To run tests locally, you need to set the correct environment variables via a .env file. Ask the author to share one at [ierofeev.qa@gmail.com]()**


Python is required to run the frontend tests:

https://www.python.org/downloads/

- Before running the tests, create virtual env and install the dependencies by running

```sh
python3 -m venv venv  
```

```sh
source venv/bin/activate 
```

```sh
pip install -r requirements.txt 
```


- To run the tests use command. This command will run tests in parallel and headed modes


```sh
pytest --alluredir=allure-results ./tests --numprocesses 2 --headed
```


- To run linter use command

```sh
mypy .
```

- To generate and open Аllure report after test run use commands

```sh
allure serve allure-results
```

When running in CI, the Allure report is generated automatically and is available as a run artifact