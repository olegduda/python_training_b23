# -*- coding: utf-8 -*-
from model.dto_group import Group
from datetime import datetime


def test_edit_first_group(app):
    if app.group.count() < 1:
        app.group.preparation_several_group(2)
    old_groups = app.group.get_group_list()
    new_group = Group(name=f"Первая Группа изменена {datetime.now()}", header="New Edit h123", footer="Edit F5778")
    new_group.id = old_groups[0].id
    app.group.edit_first(new_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_by_name_group(app):
    app.group.preparation_several_group(4)
    old_groups = app.group.get_group_list()
    new_group = Group(name=f"Группа изменена {datetime.now()}", header="New Edit h123", footer="Edit F5778")
    new_group.id = old_groups[3].id
    app.group.edit_name(old_groups[3].name, new_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[3] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
