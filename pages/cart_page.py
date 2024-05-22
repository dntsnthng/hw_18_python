from selene import browser, have
from jsonschema import validate
from data.user import User
from schemas.schemas import picture, jewelry
from utils.api_functions import Api


class CartPage:

    def open(self, user: User):
        browser.open(user.WEB_URL)

    def login_api(self, user: User):
        r = Api()
        result = r.api_request(url=user.WEB_URL, endpoint="login", method="POST",
                               data={"Email": user.LOGIN, "password": user.PASSWORD, "RememberMe": False},
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
        r = Api()
        response = r.api_request(url=user.WEB_URL, endpoint="addproducttocart/catalog/53/1/1", method="POST")
        body = response.json()
        validate(body, schema=picture)

    def add_card_jewelry(self, user: User):
        r = Api()
        response = r.api_request(url=user.WEB_URL, endpoint="/addproducttocart/catalog/14/1/1", method="POST")
        body = response.json()
        validate(body, schema=jewelry)

    def check_card(self):
        browser.element('#topcartlink').click()
        browser.element('table.cart').should(have.text("3rd Album"))
        browser.element('table.cart').should(have.text("Black & White Diamond Heart"))
