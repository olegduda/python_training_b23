# -*- coding: utf-8 -*-

import jsonpickle
import os
import random
import string
import getopt
import sys

from model.dto_contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "files"])
except getopt.GetoptError as err:
    sys.exit(2)

number = 5
file = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        number = int(a)
    elif o == "-f":
        file = a


def random_string(prefix, max_len):
    symbol = string.digits + string.ascii_letters + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(max_len))])


test_data = [Contact(first_name="", last_name="", middle_name="")] + [
    Contact(first_name=random_string("first_name", 15),
            last_name=random_string("last_name", 15),
            middle_name=random_string("middle_name", 15))
    for i in range(number)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file)

with open(file, "w") as file_json:
    # file_json.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    file_json.write(jsonpickle.encode(test_data))
