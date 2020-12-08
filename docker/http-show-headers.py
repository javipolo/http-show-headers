#!/usr/bin/env python3

from bottle import route, run, request
from json import dumps
from os import environ

# Where to listen on HTTP
address = '0.0.0.0'
port = 8080


@route('/healthz')
def get_health():
    return "true"


@route('/:#.*#', method='ANY')
def print_headers():
    my_dict = {}
    for k in request.headers:
        my_dict[k] = request.headers[k]
    if 'DEBUG' in environ:
        if environ['DEBUG'] == 'true':
            print(dumps(my_dict, sort_keys=True))
            postdata = request.body.read()
            if postdata != "":
                print(postdata)
    return dumps(my_dict, sort_keys=True, indent=2) + "\n"


if __name__ == '__main__':
    if 'DEBUG' in environ and environ['DEBUG'] == 'true':
        run(host=address, port=port, quiet=True)
    else:
        run(host=address, port=port)
