import requests
from requests import Response
import logging
import allure
from allure_commons.types import AttachmentType
import json


class Api:

    def api_request(self, url, endpoint, method, data=None, params=None, allow_redirects=None):
        url = f"{url}{endpoint}"
        response = requests.request(method, url, data=data, params=params, allow_redirects=allow_redirects)
        self.response_logging(response)
        self.response_attaching(response)
        return response

    def response_logging(self, response: Response):
        logging.info("Request: " + response.request.url)

        if response.request.body:
            logging.info("INFO Request body: " + response.request.body)
        logging.info("Request headers: " + str(response.request.headers))
        logging.info("Response code " + str(response.status_code))
        logging.info("Response: " + response.text)

    def response_attaching(self, response: Response):
        allure.attach(
            body=response.request.url,
            name="Request url",
            attachment_type=AttachmentType.TEXT,
        )

        if response.request.body:
            allure.attach(
                body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
                name="Request body",
                attachment_type=AttachmentType.JSON,
                extension="json",
            )
            allure.attach(
                body=response.text,
                name='response.text',
                attachment_type=AttachmentType.TEXT,
                extension=".txt"
            )
