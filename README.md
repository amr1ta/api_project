## Day 0
- interacting programmatically with an API using requests library
- Added class Api_Calls and added functions for methods, GET,PUT,PATCH,POST and DELETE using httpx library

## Day 1
- Built tests for the API calls using pytest

## Day 2
- Built test class with test functions for the API calls using pytest
- Passed argument from one test function to another within test class
- Parameterized test functions using @pytest.mark.parametrize decorator

## Day 3
- Added `conftest.py` to pass test data to test class using @pytest.fixture() decorator.

## Day 4
- Require authorization to access employees (formerly users) endpoint.
- Used requests.sessions to set set Authorization header details in class Api_Client
- Added fixture to instantiate Api_Client class in `test_api_methods.py`

## Day 5
- Pass test arguments from command line