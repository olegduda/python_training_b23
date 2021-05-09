# -*- coding: utf-8 -*-

from model.dto_group import Group
from datetime import datetime

    
def test_add_group(app):
    app.group.create(Group(name=f"Группа {datetime.now()}", header="New h123", footer="F5778"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
