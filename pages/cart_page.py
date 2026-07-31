from playwright.sync_api import Page
import config
from constants import routes
class CartPage:
    def __init__(self,page):
        self.page = page
        self.cart_page_heading = page.get_by_text("Your Cart")

    def open(self):
        self.page.goto(config.BASE_URL + routes.CART_PAGE)

    def get_num_of_items_in_cart(self):
       num_of_items_in_cart = self.page.locator(".cart_item").count()
       return num_of_items_in_cart

    def get_name_of_item_in_cart(self):
        name_of_item_in_cart = self.page.locator(".inventory_item_name").text_content()
        return name_of_item_in_cart

    def get_price_of_item_in_cart(self):
        price_of_item = self.page.locator(".inventory_item_price").text_content()
        return price_of_item

    def quantity_of_item_in_cart(self):
        quantity_of_item = self.page.locator('[data-test="item-quantity"]').text_content()
        return quantity_of_item