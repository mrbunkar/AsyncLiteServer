class Response:
    METHOD_NOT_ALLOWED_RESPONSE = b"""\
HTTP/1.1 405 Method Not Allowed\r
Content-Type: text/plain\r
Content-Length: 17\r
\r
Method Not Allowed"""

    NOT_FOUND_RESPONSE = b"""\
HTTP/1.1 404 Not Found\r
Content-Type: text/plain\r
Content-Length: 9\r
\r
Not Found"""

    BAD_REQUEST_RESPONSE = b"""\
HTTP/1.1 400 Bad Request\r
Content-Type: text/plain\r
Content-Length: 11\r
\r
Bad Request"""

    RESPONSE = b"""\
HTTP/1.1 200 OK\r
Content-Type: text/html\r
Content-Length: 15\r
\r
<h1>Hello!</h1>"""
    
    FILE_RESPONSE_TEMPLATE = """\
HTTP/1.1 200 OK\r
Content-Type: {content_type}\r
Content-Length: {content_length}\r
\r
"""