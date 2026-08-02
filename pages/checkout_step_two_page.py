import config
from constants import routes

class CheckoutTwoPage:
    def __init__(self,page):
        self.page = page
        self.header = page.locator(".header_secondary_container .title")
        self.finish_button = page.get_by_role("button",name="Finish")
        self.cancel_button = page.get_by_role("button",name="Cancel")

    def open(self):
        self.page.goto(config.BASE_URL+routes.CHECKOUT_STEP_TWO_PAGE)

    def get_name_of_in_final_cart(self):
        name_of_prod = self.page.locator(".inventory_item_name").text_content()
        return name_of_prod