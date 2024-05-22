import allure
from pages.cart_page import CartPage



@allure.tag('web')
@allure.title('Successful login')
def test_demowebshop():
    cart = CartPage()
    cart.login_api()


@allure.title('Add pictures in cart')
def test_add_pictures():
    cart = CartPage()
    cart.add_card_picture()


@allure.title('Add jewelry in cart')
def test_add_fl():
    cart = CartPage()
    cart.add_card_jewelry()


@allure.title('Check cart')
def test_check_shop():
    cart = CartPage()
    cart.test_check_cart()


