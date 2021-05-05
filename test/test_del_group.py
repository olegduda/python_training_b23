# -*- coding: utf-8 -*-


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.preparation_several_group(5)
    app.group.delete_first()
    app.session.logout()


def test_delete_by_name_group(app):
    app.session.login(username="admin", password="secret")
    groups_name = app.group.preparation_several_group(8)
    app.group.delete_name(groups_name[4])
    app.session.logout()
