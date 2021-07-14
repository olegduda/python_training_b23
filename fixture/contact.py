import re

from model.dto_contact import Contact
from selenium.webdriver.support.ui import Select
from time import sleep
from fixture.application import Application


class ContactHelper:
    
    def __init__(self, app: Application):
        self.app = app
    
    def return_home_page(self):
        wd = self.app.wd
        if not self.is_home_page():
            wd.find_element_by_link_text("home page").click()

    def menu_home(self):
        wd = self.app.wd
        if not self.is_home_page():
            wd.find_element_by_link_text("home").click()
        
    def open_add_contact_page(self):
        wd = self.app.wd
        if not self.is_contact_page():
            wd.find_element_by_link_text("add new").click()

    def is_home_page(self):
        wd = self.app.wd
        return wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0

    def is_contact_page(self):
        wd = self.app.wd
        return wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("firstname")) > 0

    def add_contact(self, contact: Contact) -> None:
        wd = self.app.wd
        self.open_add_contact_page()
        self._fill_fields(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()
        self.contact_cache = None

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.menu_home()
        self.select_by_index(index)
        wd.find_element_by_xpath(f"//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.menu_home()
        self.contact_cache = None

    def delete_all(self):
        wd = self.app.wd
        self.menu_home()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath(f"//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.menu_home()
        self.contact_cache = None

    def edit_first(self, contact: Contact):
        self.edit_by_index(0, contact)

    def edit_by_index(self, index: int, contact: Contact):
        wd = self.app.wd
        self.menu_home()
        wd.find_elements_by_xpath(f"//tr[not(@style) and @name='entry']//img[@title='Edit']")[index].click()
        self._fill_fields(contact)
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None

    def search(self, to_find: str):
        wd = self.app.wd
        wd.find_element_by_name("searchstring").click()
        wd.find_element_by_name("searchstring").click()
        wd.find_element_by_name("searchstring").send_keys(to_find)
        sleep(2)

    def preparation_several_contacts(self, quantity: int) -> []:
        contacts = []
        for number in range(quantity):
            contact = Contact()
            contacts.append(contact)
            self.add_contact(contact)
        return contacts

    def _fill_fields(self, contact: Contact):
        self._change_field_text_value("firstname", contact.first_name)
        self._change_field_text_value("middlename", contact.middle_name)
        self._change_field_text_value("lastname", contact.last_name)
        self._change_field_text_value("nickname", contact.nickname)
        self._change_field_text_value("title", contact.title)
        self._change_field_text_value("company", contact.company)
        self._change_field_text_value("address", contact.address)
        self._change_field_text_value("home", contact.phone_home)
        self._change_field_text_value("mobile", contact.phone_mobile)
        self._change_field_text_value("work", contact.phone_work)
        self._change_field_text_value("fax", contact.phone_fax)
        self._change_field_text_value("email", contact.email_one)
        self._change_field_text_value("email2", contact.email_two)
        self._change_field_text_value("email3", contact.email_three)
        self._change_field_text_value("homepage", contact.home_page)

        self._change_field_select_value("bday", contact.b_day, f"//option[@value='{contact.b_day}']")
        self._change_field_select_value("bmonth", contact.b_month, f"//option[@value='{contact.b_month}']")
        self._change_field_text_value("byear", contact.b_year)

        self._change_field_select_value("aday", contact.a_day,
                                        f"(//option[@value='{contact.a_day}' and not(@selected)])")
        self._change_field_select_value("amonth", contact.a_month,
                                        f"(//option[@value='{contact.a_month}' and not(@selected)])")
        self._change_field_text_value("ayear", contact.a_year)

        self._change_field_select_value("new_group", contact.group, f"(//option[text() = '{contact.group}'])")

        self._change_field_text_value("address2", contact.address_two)
        self._change_field_text_value("phone2", contact.phone_2)
        self._change_field_text_value("notes", contact.notes)

    def _change_field_text_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def _change_field_select_value(self, field_name, value, xpath):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)
            wd.find_element_by_xpath(xpath).click()

    def count(self):
        wd = self.app.wd
        self.menu_home()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.menu_home()
            self.contact_cache = []
            for row in wd.find_elements_by_css_selector("tr[name='entry']"):
                cells = row.find_elements_by_tag_name("td")
                id_contact = cells[0].find_element_by_tag_name("input").get_attribute("value")
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                all_phones_list = all_phones.splitlines()
                phone_home, phone_mobile, phone_work, phone_2 = None, None, None, None
                for index in range(0, len(all_phones_list)):
                    if index == 0:
                        phone_home = all_phones_list[0]
                    if index == 1:
                        phone_mobile = all_phones_list[1]
                    if index == 2:
                        phone_work = all_phones_list[2]
                    if index == 3:
                        phone_2 = all_phones_list[3]
                self.contact_cache.append(Contact(last_name=last_name, first_name=first_name,
                                                  id_contact=id_contact,
                                                  address=address,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones,
                                                  phone_home=phone_home, phone_work=phone_work,
                                                  phone_mobile=phone_mobile, phone_2=phone_2,
                                                  all_none=True))
        return list(self.contact_cache)

    def open_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.menu_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.menu_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        id_contact = wd.find_element_by_name("id").get_attribute("value")
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone_fax = wd.find_element_by_name("fax").get_attribute("value")
        phone_2 = wd.find_element_by_name("phone2").get_attribute("value")
        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id_contact=id_contact, first_name=first_name, last_name=last_name, address=address,
                       phone_home=phone_home, phone_work=phone_work, phone_mobile=phone_mobile, phone_fax=phone_fax,
                       phone_2=phone_2,
                       email_one=email_1, email_two=email_2, email_three=email_3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        view_text = wd.find_element_by_id("content").text
        phone_home = re.search("H: (.*)", view_text).group(1)
        phone_work = re.search("W: (.*)", view_text).group(1)
        phone_mobile = re.search("M: (.*)", view_text).group(1)
        phone_2 = re.search("P: (.*)", view_text).group(1)
        return Contact(phone_home=phone_home, phone_work=phone_work, phone_mobile=phone_mobile, phone_2=phone_2)

    def get_count_contacts_from_counter(self) -> int:
        wd = self.app.wd
        try:
            count = int(wd.find_element_by_id("search_count").text)
        except ValueError as e:
            print(f"Это не число: {e}")
        return count
