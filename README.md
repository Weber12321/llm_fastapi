# llm_fastapi

## System requirement
+ Ubuntu 22.4
+ Python 3.10

## Setup
+ Clone the repo: 
```
$ git clone https://github.com/Weber12321/llm_fastapi.git
```
+ Setup environments: 
```
$ cd llm_fastapi/

$ python -m venv venv

$ source venv/bin/activate

$ pip install requirments
```
+ Run service
```
$ fastapi dev main.py
```
+ See the api endpoint information via `/docs`:
`localhost:8000/docs`