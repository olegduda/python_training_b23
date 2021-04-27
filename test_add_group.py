# -*- coding: utf-8 -*-

from selenium import webdriver

from helpers.base_methods_ui import BaseMethodsUI
from helpers.dto_group import Group
from datetime import datetime
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.home_page_url = "http://localhost/addressbook/"
    
    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd, page=self.home_page_url)
        BaseMethodsUI.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, Group(name=f"Группа {datetime.now()}", header="New h123", footer="F5778"))
        self.open_group_page(wd)
        BaseMethodsUI.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd, page=self.home_page_url)
        BaseMethodsUI.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        self.open_group_page(wd)
        BaseMethodsUI.logout(wd)

    @staticmethod
    def create_group(wd, group: Group) -> None:
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

    @staticmethod
    def open_group_page(wd):
        wd.find_element_by_link_text("groups").click()

    @staticmethod
    def open_home_page(wd, page: str) -> None:
        wd.get(page)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
