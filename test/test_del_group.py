# -*- coding: utf-8 -*-
from model.dto_group import Group
from random import randrange


def test_delete_first_group(app):
    if app.group.count() < 1:
        app.group.preparation_several_group(2)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.pop(index)
    assert old_groups == new_groups


def test_delete_by_name_group(app):
    groups_name = app.group.preparation_several_group(3)
    old_groups = app.group.get_group_list()
    group_delete = groups_name[2]
    app.group.delete_by_name(group_delete)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.remove(Group.found_by_name_in_list(name=group_delete, list_group=old_groups))
    assert old_groups == new_groups
