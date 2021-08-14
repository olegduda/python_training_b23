# -*- coding: utf-8 -*-
import json
import jsonpickle
import os
import random
import string
import getopt
import sys

from model.dto_group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "files"])
except getopt.GetoptError as err:
    # getopt.usage() # - отсуствует в getopt
    sys.exit(2)

number = 5
file = "data/groups.json"

for o, a in opts:
    if o == "-n":
        number = int(a)
    elif o == "-f":
        file = a


def random_string(prefix, max_len):
    symbol = string.digits + string.ascii_letters + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(max_len))])


test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("first_name", 15),
          header=random_string("last_name", 15),
          footer=random_string("middle_name", 15))
    for i in range(number)
]

test_data_cross = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 20)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file)

with open(file, "w") as file_json:
    # file_json.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    file_json.write(jsonpickle.encode(test_data))
