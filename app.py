# -*- coding: utf-8 -*-
import os
import requests
from werkzeug.utils import redirect
from werkzeug.wrappers import Request, Response


DEFAULT_TARGET = 'http://localhost:8080'
HTTP_TEMPORARY_REDIRECT = 303


def application(environ, start_response):
    request = Request(environ)
    target = request.args.get('target', DEFAULT_TARGET)
    return redirect(target, code=HTTP_TEMPORARY_REDIRECT)


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    run_simple('localhost', port, application)