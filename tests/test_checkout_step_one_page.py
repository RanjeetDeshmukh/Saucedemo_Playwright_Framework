from playwright.sync_api import expect
import re
from constants.routes import CHECKOUT_STEP_ONE_PAGE,CHECKOUT_STEP_TWO_PAGE
from test_data.users import VALID_USER
from test_data.checkout_users import VALID_CHECKOUT_USER

def test_user_can_open_checkout_info_page(login_page,inventory_page,cart_page,checkout_step_one_page):
    login_page.open()
    login_page.login(VALID_USER["username"],VALID_USER["password"])
    inventory_page.add_fleece_jacket_to_cart()
    inventory_page.open_shopping_cart()
    cart_page.proceed_to_checkout()

    #assert we are on checkout info page
    expect(checkout_step_one_page.page).to_have_url(re.compile(fr"{CHECKOUT_STEP_ONE_PAGE}"))

    expect(checkout_step_one_page.header).to_have_text("Checkout: Your Information")

    #assert firstname,lastnmae,pincode fields are visible

    expect(checkout_step_one_page.first_name_field).to_be_visible()
    expect(checkout_step_one_page.last_name_field).to_be_visible()
    expect(checkout_step_one_page.postal_code_field).to_be_visible()

    #assert continue & cancel button are visible
    expect(checkout_step_one_page.continue_button).to_be_visible()
    expect(checkout_step_one_page.cancel_button).to_be_visible()

