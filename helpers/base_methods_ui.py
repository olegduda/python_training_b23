class BaseMethodsUI:

    def __init__(self, wd):
        self.wd = wd

    home_page_url = "http://localhost/addressbook/"

    def login(self, username: str, password: str) -> None:
        self.open_home_page(self.home_page_url)
        self.wd.find_element_by_name("user").click()
        self.wd.find_element_by_name("user").clear()
        self.wd.find_element_by_name("user").send_keys(username)
        self.wd.find_element_by_name("pass").clear()
        self.wd.find_element_by_name("pass").send_keys(password)
        self.wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, page: str) -> None:
        self.wd.get(page)

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()
