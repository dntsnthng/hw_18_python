import allure
from pages.cart_page import shop


@allure.tag('web')
@allure.title('Successful login')
def test_demowebshop():
    shop.login_api()


@allure.title('Add pictures in cart')
def test_add_pictures():
    shop.add_card_picture()


@allure.title('Add jewelry in cart')
def test_add_fl():
    shop.add_card_jewelry()


@allure.title('Check cart')
def test_check_shop():
    shop.test_check_cart()
