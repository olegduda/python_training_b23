from model.dto_contact import Contact
import re


def test_phone_from_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.phone_home == clear(contact_from_edit_page.phone_home)
    assert contact_from_home_page.phone_work == clear(contact_from_edit_page.phone_work)
    assert contact_from_home_page.phone_mobile == clear(contact_from_edit_page.phone_mobile)
    assert contact_from_home_page.phone_2 == clear(contact_from_edit_page.phone_2)


def test_phone_from_view_page(app):
    contact_from_home_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.phone_home == contact_from_edit_page.phone_home
    assert contact_from_home_page.phone_work == contact_from_edit_page.phone_work
    assert contact_from_home_page.phone_mobile == contact_from_edit_page.phone_mobile
    assert contact_from_home_page.phone_2 == contact_from_edit_page.phone_2


def test_phone_from_home_page_revers(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(string):
    string = re.sub("^00", "+", string)
    string = re.sub("-0", "", string)
    return re.sub("[(). -]", "", string)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.phone_home, contact.phone_mobile,
                                        contact.phone_work, contact.phone_2]))))
