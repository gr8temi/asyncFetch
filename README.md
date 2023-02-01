# Asynchronous Fetch

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/gr8temi/asyncFetch.git
$ cd asyncFetch
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv myvenv
$ source myvenv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Endpoints


```
1. To retrieve data asynchronously: 
    GET 'http://127.0.0.1:8000/'
    returns 
    {
        quotes: Result from quotable page 1,
        user: result from calling the random user endpoint
    }
```