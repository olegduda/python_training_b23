# -*- coding: utf-8 -*-

from helpers.dto_group import Group
from datetime import datetime

    
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name=f"Группа {datetime.now()}", header="New h123", footer="F5778"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()


