# -*- coding: utf-8 -

from model.dto_contact import Contact


def test_add_user(app):
    group_name = app.group.preparation_group()
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(Contact(group=group_name))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_user_space_name(app):
    group_name = app.group.preparation_group()
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(Contact(group=group_name))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

