# -*- coding: utf-8 -*-


def test_delete_first_group(app):
    if app.group.count() < 1:
        app.group.preparation_several_group(2)
    old_groups = app.group.get_group_list()
    app.group.delete_first()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)


def test_delete_by_name_group(app):
    groups_name = app.group.preparation_several_group(8)
    old_groups = app.group.get_group_list()
    app.group.delete_name(groups_name[4])
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
