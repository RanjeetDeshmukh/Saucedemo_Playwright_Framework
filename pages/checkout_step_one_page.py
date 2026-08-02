import config
from constants import routes
class CheckoutOnePage:
    def __init__(self,page):
        self.page = page
        self.header = page.locator(".header_secondary_container .title")
        self.first_name_field = page.get_by_placeholder("First Name")
        self.last_name_field = page.get_by_placeholder("Last Name")
        self.postal_code_field = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.locator("#continue")
        self.cancel_button = page.get_by_role("button",name="Cancel")

    def open(self):
        self.page.goto(config.BASE_URL+routes.CHECKOUT_STEP_ONE_PAGE)


