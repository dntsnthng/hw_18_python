import os

from selene import browser, have
from jsonschema import validate

from schemas.json import picture, jewelry
from utils.api_functions import Api
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASS = os.getenv("PASS")
URL = "https://demowebshop.tricentis.com/"



class CartPage:

    def open(self):
        browser.open(URL)

    def login_api(self):
        login_with = Api()
        result = login_with.api_request(url=URL, endpoint="login", method="POST",
                               data={"Email": EMAIL, "password": PASS, "RememberMe": False},
                               allow_redirects=False)

        print(result.text)
        print(result.cookies)
        cookie = result.cookies.get("NOPCOMMERCE.AUTH")

        browser.open(URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(URL)

    def login(self):
        browser.element('.ico-login').click()
        browser.element('#Email').send_keys(EMAIL).press_enter()
        browser.element('#Password').send_keys(PASS).click()
        browser.element('.button-1.login-button').click()

    def add_card_picture(self):
        r = Api()
        response = r.api_request(url=URL, endpoint="addproducttocart/catalog/53/1/1", method="POST")
        body = response.json()
        validate(body, schema=picture)

    def add_card_jewelry(self):
        r = Api()
        response = r.api_request(url=URL, endpoint="/addproducttocart/catalog/14/1/1", method="POST")
        body = response.json()
        validate(body, schema=jewelry)

    def check_card(self):
        browser.element('#topcartlink').click()
        browser.element('table.cart').should(have.text("3rd Album"))
        browser.element('table.cart').should(have.text("Black & White Diamond Heart"))
