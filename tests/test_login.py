import allure

from page.cart import CartPage
from data.user import user


@allure.tag('web')
@allure.title('Successful login')
def test_demowebshop():
    cart = CartPage()
    cart.login_api(user)


@allure.title('Add pictures in cart')
def test_add_pictures():
    cart = CartPage()
    cart.add_card_picture(user)


@allure.title('Add jewelry in cart')
def test_add_fl():
    cart = CartPage()
    cart.add_card_jewelry(user)


@allure.title('Check cart')
def test_check_cart():
    cart = CartPage()
    cart.open()
    cart.login(user)
    cart.check_card()