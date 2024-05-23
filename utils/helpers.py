from requests import Response
import logging
import allure
from allure_commons.types import AttachmentType
import json


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)

    if response.request.body:
        logging.info("INFO Request body: " + response.request.body)
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


def response_attaching(response: Response):
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


