import re
from playwright.sync_api import expect
from test_data.users import VALID_USER
from constants import routes

def test_product_in_cart(login_page,inventory_page,cart_page):
    login_page.open()
    login_page.login(VALID_USER["username"],VALID_USER["password"])
    inventory_page.add_fleece_jacket_to_cart()
    name_of_prod_added_to_cart = inventory_page.get_name_of_product_added_to_cart()
    price_of_prod_added_to_cart = inventory_page.get_price_of_product_added_to_cart()
    inventory_page.open_shopping_cart()

    #assert cart page is opened
    expect(cart_page.page).to_have_url(re.compile(fr"{routes.CART_PAGE}"))

    #assert 1 item is present into the cart
    assert cart_page.get_num_of_items_in_cart() == 1

    #assert the item we added & the item in cart is same
    assert name_of_prod_added_to_cart == cart_page.get_name_of_item_in_cart()

    #assert the price of item added & price of item in cart is same
    assert price_of_prod_added_to_cart == cart_page.get_price_of_item_in_cart()

    #assert quantity of product is 1
    assert cart_page.quantity_of_item_in_cart() == "1"

def test_removing_prod_from_cart(login_page,inventory_page,cart_page):
    login_page.open()
    login_page.login(VALID_USER["username"],VALID_USER["password"])
    inventory_page.add_fleece_jacket_to_cart()
    inventory_page.open_shopping_cart()
    name_of_item_in_cart = cart_page.get_name_of_item_in_cart()
    cart_page.remove_item_from_cart()

    #assert removed item is not present in cart
    expect(cart_page.cart_item_container.filter(has_text=name_of_item_in_cart)).to_be_hidden()



