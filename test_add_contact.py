# -*- coding: utf-8 -

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from helpers.base_methods_ui import BaseMethodsUI
from helpers.dto_contact import Contact
from helpers.data_preparation import PreparationGroup
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.home_page_url = "http://localhost/addressbook/"

    def test_add_user(self):
        wd = self.wd
        self.open_home_page(wd, page=self.home_page_url)
        BaseMethodsUI.login(wd, username="admin", password="secret")
        self.group_name = PreparationGroup.preparation_group_ui(wd)
        self.open_add_contact_page(wd)
        self.add_contact(wd, Contact(group=self.group_name))
        self.return_home_page(wd)
        BaseMethodsUI.logout(wd)

    def test_add_user_space_name(self):
        wd = self.wd
        self.open_home_page(wd, page=self.home_page_url)
        BaseMethodsUI.login(wd, username="admin", password="secret")
        self.group_name = PreparationGroup.preparation_group_ui(wd)
        self.open_add_contact_page(wd)
        self.add_contact(wd, Contact(group=self.group_name))
        self.return_home_page(wd)
        BaseMethodsUI.logout(wd)

    @staticmethod
    def return_home_page(wd):
        wd.find_element_by_link_text("home page").click()

    def add_contact(self, wd, contact: Contact) -> None:
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.phone_work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.phone_fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_one)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_two)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_three)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.home_page)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.b_day)
        wd.find_element_by_xpath(f"//option[@value='{contact.b_day}']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.b_month)
        wd.find_element_by_xpath(f"//option[@value='{contact.b_month}']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.b_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.a_day)
        wd.find_element_by_xpath(f"(//option[@value='{contact.a_day}'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.a_month)
        wd.find_element_by_xpath(f"(//option[@value='{contact.a_month}'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.a_year)
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.group)
        wd.find_element_by_xpath(f"(//option[text() = '{contact.group}'])").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address_two)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone_address_two)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    @staticmethod
    def open_add_contact_page(wd):
        wd.find_element_by_link_text("add new").click()

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
