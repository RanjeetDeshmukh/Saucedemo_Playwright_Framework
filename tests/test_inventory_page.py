import re
import config
from test_data.users import VALID_USER
from playwright.sync_api import expect
def test_user_can_logout(login_page,inventory_page):
    login_page.open()
    login_page.login(VALID_USER["username"],VALID_USER["password"])
    inventory_page.open_burger_menu()
    inventory_page.logout()
    #assert user logged out successfully & back to login page
    expect(login_page.page).to_have_url(config.BASE_URL)
    expect(login_page.login_button).to_be_visible()
