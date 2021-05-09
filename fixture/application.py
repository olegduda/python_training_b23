
from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self, base_url="http://localhost/addressbook/"):
        self.home_page_url = base_url
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self, page: str) -> None:
        wd = self.wd
        wd.get(page)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except Exception as error:
            print(f"Session error: {error.args}")
            return False


