# -*- coding: utf-8 -

from model.dto_contact import Contact


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    group_name = app.group.preparation_group()
    app.contact.add_contact(Contact(group=group_name))
    app.session.logout()


def test_add_user_space_name(app):
    app.session.login(username="admin", password="secret")
    group_name = app.group.preparation_group()
    app.contact.add_contact(Contact(group=group_name))
    app.session.logout()

