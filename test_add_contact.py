# -*- coding: utf-8 -

from helpers.dto_contact import Contact
from helpers.data_preparation import PreparationGroup


def test_add_user(app):
    app.login(username="admin", password="secret")
    group_name = PreparationGroup.preparation_group_ui(app)
    app.add_contact(Contact(group=group_name))
    app.logout()


def test_add_user_space_name(app):
    app.login(username="admin", password="secret")
    group_name = PreparationGroup.preparation_group_ui(app)
    app.add_contact(Contact(group=group_name))
    app.logout()

