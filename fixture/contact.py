from model.dto_contact import Contact
from selenium.webdriver.support.ui import Select
from time import sleep


class ContactHelper:
    
    def __init__(self, app):
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

    def delete_first(self):
        wd = self.app.wd
        self.menu_home()
        wd.find_element_by_name("selected[]").click()
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
        wd = self.app.wd
        self.menu_home()
        wd.find_element_by_xpath(f"//tr[not(@style)]//img[@title='Edit']").click()
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
        self._change_field_text_value("phone2", contact.phone_address_two)
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
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id_contact = element.find_element_by_xpath("td[1]/input").get_attribute("value")
                last_name = element.find_element_by_xpath("td[2]").text
                first_name = element.find_element_by_xpath("td[3]").text
                self.contact_cache.append(Contact(last_name=last_name, first_name=first_name,
                                             id_contact=id_contact, all_none=True))
        return list(self.contact_cache)

