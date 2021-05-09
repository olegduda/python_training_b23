# -*- coding: utf-8 -

from model.dto_contact import Contact


def test_add_user(app):
    group_name = app.group.preparation_group()
    app.contact.add_contact(Contact(group=group_name))


def test_add_user_space_name(app):
    group_name = app.group.preparation_group()
    app.contact.add_contact(Contact(group=group_name))

