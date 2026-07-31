from platform import ios_ver

import config
import re
from test_data.users import VALID_USER
from constants.routes import INVENTORY_PAGE
from playwright.sync_api import expect

def test_user_can_logout(login_page,inventory_page):
    login_page.open()
    login_page.login(VALID_USER["username"],VALID_USER["password"])
    inventory_page.open_burger_menu()
    inventory_page.logout()
    #assert user logged out successfully & back to login page
    expect(login_page.page).to_have_url(config.BASE_URL)
    expect(login_page.login_button).to_be_visible()

def test_inventory_has_products(login_page,inventory_page):
    login_page.open()
    login_page.login(VALID_USER["username"], VALID_USER["password"])

    #assert user is on inventory page
    expect(inventory_page.page).to_have_url(re.compile(fr"{INVENTORY_PAGE}"))

    #assert at least one product is present in inventory
    expect(inventory_page.inventory_list).to_be_visible()

    num_of_products = inventory_page.products_count()
    assert num_of_products != 0

def test_can_add_product_to_cart(login_page,inventory_page):
    login_page.open()
    login_page.login(VALID_USER["username"], VALID_USER["password"])
    inventory_page.add_fleece_jacket_to_cart()

    #assert the cart shows badge as 1

    expect(inventory_page.shopping_cart_badge).to_have_text("1")
    expect(inventory_page.shopping_cart_link).to_be_visible()

def test_remove_added_product(login_page,inventory_page):
    login_page.open()
    login_page.login(VALID_USER["username"], VALID_USER["password"])
    inventory_page.add_fleece_jacket_to_cart()
    product_added_to_cart = inventory_page.get_name_of_product_added_to_cart()


    # assert the cart shows badge as 1
    expect(inventory_page.shopping_cart_badge).to_have_text("1")

    inventory_page.remove_added_product()

    #assert shopping cart badge is no longer displayed
    expect(inventory_page.shopping_cart_badge).not_to_be_attached()

    #assert the item has Add to cart button
    expect(inventory_page.item_description_container.filter(has_text=product_added_to_cart)).to_contain_text("Add to cart")


