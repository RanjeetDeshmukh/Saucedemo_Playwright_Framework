from playwright.sync_api import expect
from test_data.users import VALID_USER, INVALID_USER
import re
import config
from constants.routes import INVENTORY_PAGE

def test_valid_user_can_login(login_page,inventory_page):
    login_page.open()
    login_page.login(VALID_USER["username"],VALID_USER["password"])

    #assert user logged successfully & navigated to inventory page
    expect(inventory_page.page).to_have_url(re.compile(fr"{INVENTORY_PAGE}"))
    expect(inventory_page.header).to_have_text("Products")

def test_invalid_user_cant_login(login_page):
    login_page.open()
    login_page.login(INVALID_USER["username"],INVALID_USER["password"])

    #assert user does not login & correct error message is displayed
    expect(login_page.error_msg_container).to_contain_text("Username and password do not match")
    expect(login_page.page).to_have_url(config.BASE_URL)
