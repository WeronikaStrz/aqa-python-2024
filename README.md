# Description
### Testing github.com login page.
This is an educational project owned by Weronika Strzelczyk. It is in development, during Python Academy GlobalLogic in 2024. 

## How to set up the environment locally

### What is needed:
- Python version 3.11.7
- Poetry version 1.8.2

### How to install dependencies

 `poetry install`

### How to run
To run tests: `poetry run pytest`

### Development
Install and run pre-commit locally before each new commit: `pre-commit run --all-files`

## Structure of framework
1. src/applications - system under tests abstraction

2. tests - tests for system

3. reports - automatically generated local test reports

4. src/config - configuration of framework

5. src/helpers - single-use functions
