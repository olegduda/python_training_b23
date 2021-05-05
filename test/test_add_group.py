# -*- coding: utf-8 -*-

from model.dto_group import Group
from datetime import datetime

    
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name=f"Группа {datetime.now()}", header="New h123", footer="F5778"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


