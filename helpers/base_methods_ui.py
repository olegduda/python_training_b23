class BaseMethodsUI:

    @staticmethod
    def login(wd, username: str, password: str) -> None:
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    @staticmethod
    def logout(wd):
        wd.find_element_by_link_text("Logout").click()
