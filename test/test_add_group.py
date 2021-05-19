# -*- coding: utf-8 -*-

from model.dto_group import Group
from datetime import datetime

    
def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name=f"Группа {datetime.now()}", header="New h123", footer="F5778"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
