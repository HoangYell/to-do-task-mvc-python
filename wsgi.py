# -*- coding: utf-8 -*-
from controller import index, edit, delete, calendar
from router import Router
from utils import parse_http_x_www_form_urlencoded_post_data
from utils import parse_http_get_data
from utils import parse_http_headers
from utils import parse_http_content_type
from utils import parse_http_uri


# ===========================
#
#    0.0 WSGI application
#
# ===========================


DEBUG = True
STATIC_URL = '/static/'
STATIC_ROOT = 'data'

router = Router()
router.register_controller('/', index)
router.register_controller('/edit/', edit)
router.register_controller('/delete/', delete)
router.register_controller('/calendar/', calendar)

def application(environ, start_response):
    # https://www.python.org/dev/peps/pep-3333/#environ-variables
    REQUEST_METHOD = environ['REQUEST_METHOD']
    CONTENT_TYPE, CONTENT_TYPE_KWARGS = parse_http_content_type(environ)
    SERVER_PROTOCOL = environ['SERVER_PROTOCOL']
    HEADERS = parse_http_headers(environ)
    URI_PATH = environ['PATH_INFO']
    URI = parse_http_uri(environ)
    POST = parse_http_x_www_form_urlencoded_post_data(environ)
    GET = parse_http_get_data(environ)

    if URI_PATH.startswith(STATIC_URL):
        print('STATIC FILE DETECTED!',URI_PATH)
        try:
            body = open(URI_PATH[1:], 'rb').read()
            start_response('200 OK',[])
            return [body]
        except IOError:
            start_response("500 Internal Error",[])
            return []
    else:
        headers = [('Content-type', 'text/html; charset=utf-8')]
        controller_callback = router.resolve(URI_PATH)
        status, body = controller_callback(REQUEST_METHOD, GET, POST, headers)
        if DEBUG:
            print("======>\n{REQUEST_METHOD} {URI_PATH} {SERVER_PROTOCOL}\n"
                "CONTENT_TYPE: {CONTENT_TYPE}; {CONTENT_TYPE_KWARGS}\n"
                "POST: {POST}\n"
                "GET: {GET}\n"
                ":HEADERS:\n{HEADERS}\n"
                .format(**locals()))

        start_response(status, headers)
        return [body]
