from model.dto_group import Group
from faker import Faker

fake = Faker()


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group: Group) -> None:
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_group_page()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def preparation_group(self) -> str:
        group_name = f"New_{fake.isbn13(separator='-')}"
        self.open_group_page()
        self.create(group=Group(name=f"{group_name}", header="1", footer="2"))
        return group_name
