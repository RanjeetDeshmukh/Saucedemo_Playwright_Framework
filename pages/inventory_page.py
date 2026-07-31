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
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")
        self.item_description_container = page.locator(".inventory_item_description")

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

    def add_fleece_jacket_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-fleece-jacket").click()

    def get_name_of_product_added_to_cart(self):
        description = self.item_description_container.filter(has=self.page.get_by_role("button",name="Remove"))
        name_of_produce_added = description.locator(".inventory_item_name ").text_content()
        return name_of_produce_added

    def get_price_of_product_added_to_cart(self):
        description = self.item_description_container.filter(has=self.page.get_by_role("button",name="Remove"))
        price_of_product = description.locator(".inventory_item_price").text_content()
        return price_of_product

    def remove_added_product(self):
        description = self.item_description_container.filter(has=self.page.get_by_role("button",name="Remove"))
        description.get_by_role("button",name="Remove").click()