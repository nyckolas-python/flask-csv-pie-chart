# flask-csv-pie-chart

## ⚙️ Run locally

1. Clone this repo and enter to the project folder SGM:
```
git clone copy/paste/link/to/repo

cd flask-csv-pie-chart
```

2. Install Poetry is a tool for dependency management and packaging in Python:
```
$ make install poetry
# or
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
3. Install all dependencies:
```
$ make update
# or
$ poetry update
```
4. Run the 
```
$ make start
# or
$ poetry run python wsgi.py
```
5. Deploy on Heroku, you need have an account on heroku.com
```
$ poetry export -f requirements.txt --output requirements.txt --without-hashes
$ pip install heroku
$ heroku login
$ heroku create
$ git push heroku main
$ heroku ps:scale web=1
$ heroku open
$ heroku logs --tail
```

## ✅ Task

Terms of Reference
The web page on the flask on which will be the filter for the hour (interval of months). Pie Chart distribution of countries (without showing the number of invalid values) Cumulative sum of income for each of each country (n graphs) on the x-days axis of the filter.
