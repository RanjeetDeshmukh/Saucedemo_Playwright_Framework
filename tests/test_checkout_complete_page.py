import re
from playwright.sync_api import expect
from test_data.users import VALID_USER
from test_data.checkout_users import VALID_CHECKOUT_USER
from constants.routes import CHECKOUT_COMPLETE_PAGE

def test_user_can_purchase_successfully(login_page,inventory_page,cart_page,checkout_step_one_page,checkout_step_two_page,checkout_complete_page):
    login_page.open()
    login_page.login(VALID_USER["username"],VALID_USER["password"])

    inventory_page.add_fleece_jacket_to_cart()
    inventory_page.open_shopping_cart()

    cart_page.proceed_to_checkout()

    checkout_step_one_page.save_checkout_user_info(VALID_CHECKOUT_USER["firstname"],VALID_CHECKOUT_USER["lastname"],VALID_CHECKOUT_USER["postalcode"])

    checkout_step_two_page.click_finish_button()

    #assert user is on checkout complete page
    expect(checkout_complete_page.page).to_have_url(re.compile(fr"{CHECKOUT_COMPLETE_PAGE}"))
