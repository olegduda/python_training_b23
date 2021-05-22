# -*- coding: utf-8 -

from model.dto_contact import Contact


def test_add_user(app):
    group_name = app.group.preparation_group()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(group=group_name)
    app.contact.add_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_user_space_name(app):
    group_name = app.group.preparation_group()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="", group=group_name)
    app.contact.add_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

