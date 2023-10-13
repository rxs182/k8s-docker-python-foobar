import requests


def do_something(x):
    url = 'https://eo79uqts4j410f.m.pipedream.net'
    res = requests.post(url, json={'value': x}, verify=False)
    val = res.json()
    return val.get('value')


def handle_ok(job, connection, result, *args, **kwargs):
    print(f'job: {job.id} | result: {result} | args: {job.args}')


def handle_fail(job, connection, type, value, traceback):
    print(f'job: {job.id} | failed: {value}')


def handle_stop(job, connection):
    print(f'job: {job.id} | stopped')