from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
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