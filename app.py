# -*- coding: utf-8 -*-
import os
import requests
from werkzeug.utils import redirect
from werkzeug.wrappers import Request, Response


DEFAULT_TARGET = 'http://localhost:8080'


def redirect_request(request):
    target = request.args.get('target', DEFAULT_TARGET)
    requests.post(target, data=request.form, files=request.files)


def make_response(environ, start_response):
    response = Response('Redirector activated!', mimetype='text/plain')
    return response(environ, start_response)


def application(environ, start_response):
    request = Request(environ)
    redirect_request(request)
    return make_response(environ, start_response)


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    run_simple('localhost', port, application)