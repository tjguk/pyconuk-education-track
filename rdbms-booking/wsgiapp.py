from wsgiref.util import setup_testing_defaults, shift_path_info
from wsgiref.simple_server import make_server

def page(title):
    return ["""<html>
    <head><title>{title}</title></head>
    <body>
    <h1>{title}</h1>
    </body>
    </html>
    """.format(title=title)]

def users(environ):
    return page("Users")

def rooms(environ):
    return page("Rooms")

def bookings(environ):
    return page("Bookings")

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]

    start_response(status, headers)

    param1 = shift_path_info(environ)
    if param1 == "":
        return page("Index")
    elif param1 == "users":
        return users(environ)
    elif param1 == "rooms":
        return rooms(environ)
    elif param1 == "bookings":
        return bookings(environ)
    else:
        raise RuntimeError

httpd = make_server('', 8000, simple_app)
print("Serving on port 8000...")
httpd.serve_forever()