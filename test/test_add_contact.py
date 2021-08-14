# -*- coding: utf-8 -

import pytest

from model.dto_contact import Contact
from data.contact import test_data


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


def test_add_user_in_json(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

