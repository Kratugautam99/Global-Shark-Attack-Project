import io
import sys
from Web_Deployment_Files.app import app

def handler(event, context):
    environ = {
        "REQUEST_METHOD": event.get("httpMethod", "GET"),
        "PATH_INFO": event.get("path", "/"),
        "QUERY_STRING": "",
        "SERVER_NAME": "localhost",
        "SERVER_PORT": "80",
        "wsgi.version": (1, 0),
        "wsgi.url_scheme": "http",
        "wsgi.input": io.BytesIO(event.get("body", "").encode("utf-8") if event.get("body") else b""),
        "wsgi.errors": sys.stderr,
        "wsgi.multithread": False,
        "wsgi.multiprocess": False,
        "wsgi.run_once": True,
    }
    qs = event.get("queryStringParameters")
    if qs:
        environ["QUERY_STRING"] = "&".join(f"{key}={value}" for key, value in qs.items())
    response_headers = []
    status = ""
    def start_response(s, headers, exc_info=None):
        nonlocal status, response_headers
        status = s
        response_headers = headers
    result = app(environ, start_response)
    response_body = b"".join(result).decode("utf-8")
    status_code = int(status.split()[0])
    headers_dict = {key: value for key, value in response_headers}
    return {
        "statusCode": status_code,
        "headers": headers_dict,
        "body": response_body,
    }
