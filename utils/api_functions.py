import requests
from pages.helpers import Helpers

class Api:


    def api_request(self, url, endpoint, method, data=None, params=None, allow_redirects=None):
        help = Helpers()
        url = f"{url}{endpoint}"
        response = requests.request(method, url, data=data, params=params, allow_redirects=allow_redirects)
        help.response_logging(response)
        help.response_attaching(response)
        return response
