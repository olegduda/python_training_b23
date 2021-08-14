# -*- coding: utf-8 -*-

import random
import string

from model.dto_contact import Contact


constant_data = [
    Contact(first_name="first_name_1", last_name="last_name_1", middle_name="middle_name_1"),
    Contact(first_name="first_name_2", last_name="last_name_2", middle_name="middle_name_2"),
]


def random_string(prefix, max_len):
    symbol = string.digits + string.ascii_letters + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(max_len))])


test_data = [Contact(first_name="", last_name="", middle_name="")] + [
    Contact(first_name=random_string("first_name", 15), last_name=random_string("last_name", 15),
            middle_name=random_string("middle_name", 15))
    for i in range(5)
]
