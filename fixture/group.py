from __future__ import annotations

from model.dto_group import Group
from faker import Faker
from fixture.application import *

fake = Faker()


class GroupHelper:

    def __init__(self, app: Application):
        self.app = app

    def create(self, group: Group) -> None:
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self._fill_in_fields(group)
        wd.find_element_by_name("submit").click()
        self.return_group_page()
        self.group_cache = None

    def open_group_page(self):
        wd = self.app.wd
        if not self.is_group_page():
            wd.find_element_by_link_text("groups").click()

    def return_group_page(self):
        wd = self.app.wd
        if not self.is_group_page():
            wd.find_element_by_link_text("group page").click()

    def is_group_page(self):
        wd = self.app.wd
        return wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0

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
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_group_page()
        self.group_cache = None

    def delete_by_name(self, name_group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_xpath(f"//input[@title='Select ({name_group})']").click()
        wd.find_element_by_name("delete").click()
        self.return_group_page()
        self.group_cache = None

    def edit_first(self, new_group: Group):
        self.edit_by_index(index=0, new_group=new_group)

    def edit_by_index(self, index: int, new_group: Group):
        wd = self.app.wd
        self.open_group_page()
        self.select_by_index(index)
        wd.find_element_by_name("edit").click()
        self._fill_in_fields(new_group)
        wd.find_element_by_name("update").click()
        self.return_group_page()
        self.group_cache = None

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_by_name(self, name_group: str, new_group: Group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_xpath(f"//input[@title='Select ({name_group})']").click()
        wd.find_element_by_name("edit").click()
        self._fill_in_fields(new_group)
        wd.find_element_by_name("update").click()
        self.return_group_page()
        self.group_cache = None

    def _fill_in_fields(self, group: Group):
        self._change_field_value("group_name", group.name)
        self._change_field_value("group_header", group.header)
        self._change_field_value("group_footer", group.footer)

    def _change_field_value(self, field_name, group_value):
        wd = self.app.wd
        if group_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(group_value)

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                name_group = element.text
                id_group = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=name_group, id_group=id_group))
        return list(self.group_cache)


