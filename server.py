# -*- coding: utf-8 -*-
import wsgi
from wsgiref.simple_server import make_server


# ===========================
#
#        0.1 Server
#
# ===========================


PORT = 8000

print("Open: http://127.0.0.1:{0}/".format(PORT))
httpd = make_server('', PORT, wsgi.application)
httpd.serve_forever()
