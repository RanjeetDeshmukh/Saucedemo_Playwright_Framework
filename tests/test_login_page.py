from playwright.sync_api import expect
from test_data.users import VALID_USER
import re
from constants.routes import INVENTORY_PAGE

def test_valid_user_can_login(login_page,inventory_page):
    login_page.open()
    login_page.login(VALID_USER["username"],VALID_USER["password"])

    #assert user logged successfully & navigated to inventory page
    expect(inventory_page.page).to_have_url(re.compile(fr"{INVENTORY_PAGE}"))
    expect(inventory_page.header).to_have_text("Products")
