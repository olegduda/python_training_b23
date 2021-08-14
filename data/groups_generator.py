# -*- coding: utf-8 -*-

import string
import random

from model.dto_group import Group


def random_string(prefix, max_len):
    symbol = string.digits + string.ascii_letters + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(max_len))])


test_data = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 20)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]
