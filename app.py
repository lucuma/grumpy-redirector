# -*- coding: utf-8 -*-
from werkzeug.utils import redirect
from werkzeug.wrappers import Request, Response
import requests


DEFAULT_TARGET = 'http://localhost:8080'

@Request.application
def application(request):
    target = request.args.get('target', DEFAULT_TARGET)
    r(target, data=request.form, files=request.files)
    return Response('')


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)