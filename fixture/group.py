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
        self._fill_in_fields(group)
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

    def preparation_several_group(self, quantity: int) -> []:
        groups_name = []
        for number in range(quantity):
            name = self.preparation_group()
            groups_name.append(name)
        return groups_name

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_group_page()

    def delete_name(self, name_group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_xpath(f"//input[@title='Select ({name_group})']").click()
        wd.find_element_by_name("delete").click()
        self.return_group_page()

    def edit_first(self, new_group: Group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self._fill_in_fields(new_group)
        wd.find_element_by_name("update").click()
        self.return_group_page()

    def edit_name(self, name_group: str, new_group: Group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_xpath(f"//input[@title='Select ({name_group})']").click()
        wd.find_element_by_name("edit").click()
        self._fill_in_fields(new_group)
        wd.find_element_by_name("update").click()
        self.return_group_page()

    def _fill_in_fields(self, group: Group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

