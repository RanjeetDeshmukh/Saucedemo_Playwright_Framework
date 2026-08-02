from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutOnePage
from pages.checkout_step_two_page import CheckoutTwoPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_complete_page import CheckoutCompletePage
import pytest

@pytest.fixture
def login_page(page:Page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page:Page):
    return InventoryPage(page)

@pytest.fixture
def cart_page(page:Page):
    return CartPage(page)

@pytest.fixture
def checkout_step_one_page(page:Page):
    return CheckoutOnePage(page)

@pytest.fixture
def checkout_step_two_page(page:Page):
    return CheckoutTwoPage(page)

@pytest.fixture
def checkout_complete_page(page:Page):
    return CheckoutCompletePage(page)