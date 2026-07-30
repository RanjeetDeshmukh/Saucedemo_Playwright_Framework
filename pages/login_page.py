from playwright.sync_api import Page
import config
class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.locator("#login-button")
        self.error_msg_container = page.locator(".error-message-container.error h3")

    def open(self):
        self.page.goto(config.BASE_URL)

    def enter_username(self,username):
        self.username_field.fill(username)

    def enter_password(self,password):
        self.password_field.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
