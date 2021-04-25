# -*- coding: utf-8 -*-

from selenium import webdriver
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
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, Group(name=f"Группа {datetime.now()}", header="New h123", footer="F5778"))
        self.open_group_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd, page=self.home_page_url)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        self.open_group_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_group(self, wd, group):
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

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username: str, password: str) -> None:
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd, page: str) -> None:
        wd.get(page)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
