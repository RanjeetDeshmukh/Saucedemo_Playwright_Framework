from playwright.sync_api import Page
import config
from constants import routes
class InventoryPage:
    def __init__(self,page:Page):
        self.page = page
        self.shopping_cart_link = page.locator(".shopping_cart_link")
        self.burger_menu = page.get_by_role("button",name="Open Menu")
        self.logout_button = page.get_by_role("link",name="Logout")
        self.header = page.locator(".header_secondary_container>.title")
        self.inventory_list = page.locator(".inventory_list")

    def open(self):
        self.page.goto(config.BASE_URL+routes.INVENTORY_PAGE)

    def open_shopping_cart(self):
        self.shopping_cart_link.click()

    def open_burger_menu(self):
        self.burger_menu.click()

    def logout(self):
        self.logout_button.click()

    def products_count(self):
        num_of_products = self.page.locator(".inventory_item").count()
        return num_of_products