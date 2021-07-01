# -*- coding: utf-8 -

import pytest
import random
import string

from model.dto_contact import Contact


def random_string(prefix, max_len):
    symbol = string.digits + string.ascii_letters + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(max_len))])


test_data = [Contact(first_name="", last_name="", middle_name="")] + [
    Contact(first_name=random_string("first_name", 15), last_name=random_string("last_name", 15),
            middle_name=random_string("middle_name", 15))
    for i in range(5)
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_user(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_user_with_group(app):
    group_name = app.group.preparation_group()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(group=group_name)
    app.contact.add_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

