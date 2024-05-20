import requests
from selene import browser, have
from jsonschema import validate
from data.user import User
from schemas.schemas import picture, jewelry


class CartPage:
    LOGIN = "hw_18@python.ru"
    PASSWORD = "12344321"
    WEB_URL = "https://demowebshop.tricentis.com/"
    API_URL = "https://demowebshop.tricentis.com/"

    def open(self):
        browser.open('/')



    def login_api(self, user: User):
        result = requests.post(user.WEB_URL + "login", data={"Email": user.LOGIN, "password": user.PASSWORD, "RememberMe": False},
                               allow_redirects=False)
        print(result.text)
        print(result.cookies)
        cookie = result.cookies.get("NOPCOMMERCE.AUTH")

        browser.open(user.WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(user.WEB_URL)

    def login(self,user: User):
        browser.element('.ico-login').click()
        browser.element('#Email').send_keys(user.LOGIN).press_enter()
        browser.element('#Password').send_keys(user.PASSWORD).click()
        browser.element('.button-1.login-button').click()

    def add_card_picture(self, user: User):
        response = requests.post(user.WEB_URL + "addproducttocart/catalog/53/1/1")
        body = response.json()
        validate(body, schema=picture)

    def add_card_jewelry(self, user: User):
        response = requests.post(user.WEB_URL + "addproducttocart/catalog/14/1/1")
        body = response.json()
        validate(body, schema=jewelry)

    def check_card(self):
        browser.element('#topcartlink').click()
        browser.element('table.cart').should(have.text("3rd Album"))
        browser.element('table.cart').should(have.text("Black & White Diamond Heart"))
