# -*- coding: utf-8 -*-

from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id_group=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id_group

    def __repr__(self):
        return f"{self.id}:{self.name}:{self.header}:{self.footer}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    @staticmethod
    def found_by_name_in_list(name, list_group):
        for group in list_group:
            if group.name == name:
                return group
        return None

