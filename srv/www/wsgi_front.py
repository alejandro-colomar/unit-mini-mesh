import requests

def application(environ, start_response):
    response = requests.get("htto://localhost:8081");

    start_response(response.status_code, [("Content-Type", "text/plain")]);

    return response.content;
