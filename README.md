# Github Crawler
Technical Task for a Python Developer position

- A simple program that searches on Github and returns the links from the search result.
- The purpose of this task we want to work with raw HTML and API can't be used
- Only the first page search results
- Frameworks (e.g. Scrapy) are avoided but any library can be used (e.g. HTTP libraries parser libraries)

# Input
1. Search keywords: a list of keywords to be used as search terms (unicode characters must be supported)
2. List of proxies: one of them should be selected and used randomly to perform all the HTTP requests (you can get a free list of proxies to work with at https://free-proxy-list.net/)
3. Type: the type of object we are searching for (Repositories, Issues and Wikis should be supported)

# Output
URLS for each of the results of the search

## Running on a Virtualenv (recommended)
1. First create a virtualenv
    `python3 -m venv env`
2. Activate it
    `source env/Scripts/active`
3. Install required packages
    `pip3 install -r requirements.txt`
4. Run the program passing a json file with the correct input format as the only parameter
    `python crawler.py example1.json`

## Running with Docker
Make sure you have docker installed and that the Docker daemon is running. As a default, sample input (example1.json) is being used.
- `docker build -t red-points .`
- `docker run -it -p 5000:5000 red-points`

# Tests
Python's unittest library is used.
- `python -m unittest`

# Coverage test
Make sure that coverage package is installed (pip install coverage).
- `coverage run --omit */site-packages/* -m unittest`
To see the report:
- `coverage report -m`

# example1.json
```json
{
  "keywords": [
    "openstack",
    "nova",
    "css"
  ],
  "proxies": [
    "194.126.37.94:8080",
    "13.78.125.167:8080"
  ],
  "type": "Repositories"
}
```

### Restrictions
Requires python3+ and pip3+
