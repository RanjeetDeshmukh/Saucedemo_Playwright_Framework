import config
from constants import routes
class CartPage:
    def __init__(self,page):
        self.page = page
        self.cart_page_heading = page.get_by_text("Your Cart")
            self.cart_item_container = page.locator(".cart_item")

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

    def remove_item_from_cart(self):
        cart_item = self.page.locator(".cart_item_label").filter(has_text=self.get_name_of_item_in_cart())
        cart_item.get_by_role("button",name="Remove").click()
