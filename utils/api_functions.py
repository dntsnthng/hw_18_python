import requests

from utils.helpers import helpers


def api_request(url, endpoint, method, data=None, params=None, allow_redirects=None):
    url = f"{url}{endpoint}"
    response = requests.request(method, url, data=data, params=params, allow_redirects=allow_redirects)
    helpers.response_logging(response)
    helpers.response_attaching(response)
    return response
