#!/usr/bin/env python

# Where to listen on HTTP
address = '0.0.0.0'
port = 8080

from pprint import pformat
from bottle import route, run, request, static_file
from json import dumps

@route('/healthz')
def get_health():
    return "true"


@route('/:#.*#', method='ANY')
def print_headers():
    my_dict = {}
    for k in request.headers:
        my_dict[k] = request.headers[k]
    return dumps(my_dict, sort_keys=True, indent=2)

run(host=address, port=port)