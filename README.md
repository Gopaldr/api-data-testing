\# API Data Testing



\## Overview

A simple Python project that fetches data from a REST API, parses JSON responses into a pandas DataFrame, and verifies functionality using pytest unit tests.



\## Features

\- Fetches posts using HTTP GET requests.

\- Handles HTTP errors using `raise\_for\_status()`.

\- Parses JSON data into a pandas DataFrame.

\- Tests API client behavior using mocks.

\- Validates parsed data using pytest.



\## Technologies

\- Python

\- Requests

\- Pandas

\- Pytest



\## Project Structure



api-data-testing/

├── api\_client.py

├── data\_parser.py

├── main.py

├── requirements.txt

└── tests/

&#x20;   ├── test\_api\_client.py

&#x20;   └── test\_data\_parser.py





\## Setup

Install the dependencies:





python -m pip install -r requirements.txt





\## Run the Project



python main.py





The application fetches posts and displays the first five titles.



\## Run Tests



python -m pytest -v





\## API Used

JSONPlaceholder: https://jsonplaceholder.typicode.com/posts



\## Learning Outcomes

Practiced REST API requests, JSON handling, pandas data parsing, mocking, unit testing, and debugging.

