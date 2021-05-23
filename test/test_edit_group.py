# -*- coding: utf-8 -*-
from model.dto_group import Group
from datetime import datetime
from random import randrange


def test_edit_random_group(app):
    if app.group.count() < 1:
        app.group.preparation_several_group(2)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    new_group = Group(name=f"Первая Группа изменена {datetime.now()}", header="New Edit h123", footer="Edit F5778")
    new_group.id = old_groups[index].id
    app.group.edit_by_index(index, new_group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_by_name_group(app):
    app.group.preparation_several_group(4)
    old_groups = app.group.get_group_list()
    new_group = Group(name=f"Группа изменена {datetime.now()}", header="New Edit h123", footer="Edit F5778")
    new_group.id = old_groups[3].id
    app.group.edit_by_name(name_group=old_groups[3].name, new_group=new_group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[3] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
