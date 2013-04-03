# -*- coding: utf-8 -*-
import os
import requests
from urllib import urlencode
from werkzeug.utils import redirect
from werkzeug.wrappers import Request, Response


DEFAULT_TARGET = 'http://localhost:8080/'


def redirect_request(request):
    get_args = request.args.copy()
    target = get_args.pop('target', DEFAULT_TARGET)
    query_string = urlencode(get_args)
    return redirect(target + '?' + query_string, code=307)


def application(environ, start_response):
    request = Request(environ)
    response = redirect_request(request)
    return response(environ, start_response)


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    run_simple('localhost', port, application)