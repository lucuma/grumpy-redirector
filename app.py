# -*- coding: utf-8 -*-
from werkzeug.utils import redirect
from werkzeug.wrappers import Request, Response
import requests


DEFAULT_TARGET = 'http://localhost:8080'


def redirect_request(request):
    target = request.args.get('target', DEFAULT_TARGET)
    requests.post(target, data=request.form, files=request.files)


def application(environ, start_response):
    request = Request(environ)

    if request.method == 'POST':
        redirect_request(request)

    response = Response('Redirector activated!', mimetype='text/plain')
    return response(environ, start_response)


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)