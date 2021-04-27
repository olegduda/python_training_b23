import requests
import test_add_group
from faker import Faker

fake = Faker()


class GroupApi:

    @staticmethod
    def create_group(prefix, headers=None, payload=None, parameters=None, code=200):

        # if payload is None:
        #     self.payload = f"group_name=New_{fake.isbn13(separator='-')}" \
        #                    f"&group_header=&group_footer=&submit=Enter+information"

        response = requests.post(f'{prefix}', headers=headers, data=payload, params=parameters, verify=False)
        return response
