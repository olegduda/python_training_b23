
from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd: webdriver = webdriver.Chrome()
        elif browser == "firefox":
            self.wd: webdriver = webdriver.Firefox()
        elif browser == "ie":
            self.wd: webdriver = webdriver.Ie()
        elif browser == "opera":
            self.wd: webdriver = webdriver.Opera
        else:
            raise ValueError(f"Unrecognized browser {browser}")

        self.home_page_url = base_url
        self.wd.implicitly_wait(5)

        self.session: SessionHelper = SessionHelper(self)
        self.group: GroupHelper = GroupHelper(self)
        self.contact: ContactHelper = ContactHelper(self)

    def open_home_page(self, page: str) -> None:
        wd = self.wd
        wd.get(page)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except Exception as error:
            print(f"Session error: {error.args}")
            return False


