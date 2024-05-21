import requests
from selene import browser, have
from jsonschema import validate
from data.user import User
from schemas.schemas import picture, jewelry
from requests import Response
import logging
import json
import allure
from allure_commons.types import AttachmentType


class CartPage:
    LOGIN = "hw_18@python.ru"
    PASSWORD = "12344321"
    url = "https://demowebshop.tricentis.com/"
    API_URL = "https://demowebshop.tricentis.com/"

    def open(self):
        browser.open('/')

    url = "https://demowebshop.tricentis.com/"

    def login_api(self, user: User):
        result = requests.post(user.WEB_URL + "login", data={"Email": user.LOGIN, "password": user.PASSWORD, "RememberMe": False},
                               allow_redirects=False)
        print(result.text)
        print(result.cookies)
        cookie = result.cookies.get("NOPCOMMERCE.AUTH")


        browser.open(user.WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(user.WEB_URL)

    def login(self, user: User):
        browser.element('.ico-login').click()
        browser.element('#Email').send_keys(user.LOGIN).press_enter()
        browser.element('#Password').send_keys(user.PASSWORD).click()
        browser.element('.button-1.login-button').click()

    def add_card_picture(self, user: User):
        response = self.api_request(url=user.WEB_URL, endpoint="addproducttocart/catalog/53/1/1", method="POST")
        body = response.json()
        validate(body, schema=picture)

    def add_card_jewelry(self, user: User):
        response = self.api_request (url=user.WEB_URL, endpoint="/addproducttocart/catalog/14/1/1", method="POST")
        body = response.json()
        validate(body, schema=jewelry)

    def check_card(self):
        browser.element('#topcartlink').click()
        browser.element('table.cart').should(have.text("3rd Album"))
        browser.element('table.cart').should(have.text("Black & White Diamond Heart"))





    def api_request(self, url, endpoint, method, data=None, params=None):
        url = f"{url}{endpoint}"
        response = requests.request(method, url, data=data, params=params)
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
                body=json.dumps(response.json(), indent=4, ensure_ascii=True),
                name="Response",
                attachment_type=AttachmentType.JSON,
                extension="json",
            )
