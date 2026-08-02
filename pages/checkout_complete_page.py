import config
from constants import routes

class CheckoutCompletePage:
    def __init__(self,page):
        self.page = page
        self.header = page.locator(".header_secondary_container .title")
        self.checkout_complete_msg_header = page.locator(".complete-header")
        self.back_home_button = page.get_by_role("button",name="Back Home")

    def open(self):
        self.page.goto(config.BASE_URL+routes.CHECKOUT_COMPLETE_PAGE)


