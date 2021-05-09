# -*- coding: utf-8 -*-
from model.dto_group import Group
from datetime import datetime


def test_edit_first_group(app):
    if app.group.count() < 1:
        app.group.preparation_several_group(2)
    new_group = Group(name=f"Первая Группа изменена {datetime.now()}", header="New Edit h123", footer="Edit F5778")
    app.group.edit_first(new_group)


def test_edit_by_name_group(app):
    groups_name = app.group.preparation_several_group(8)
    new_group = Group(name=f"Группа изменена {datetime.now()}", header="New Edit h123", footer="Edit F5778")
    app.group.edit_name(groups_name[4], new_group)
