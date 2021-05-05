import requests
from faker import Faker

fake = Faker()


class GroupApi:

    @staticmethod
    def create_group(prefix, headers=None, payload=None, parameters=None, cookie=None, code=200):
        prefix_add_group = f"{prefix}group.php"
        headers = {
                    'Cookie': f'{cookie.split(",")[0]}',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Referer': f'{prefix_add_group}?new=New+group',
                    'Upgrade-Insecure-Requests': '1',
                    'Connection': 'keep - alive'
                   }

        response = requests.post(f'{prefix_add_group}', headers=headers, data=payload,
                                 params=parameters, verify=False)
        return response

    @staticmethod
    def create_group_2():

        url = "http://localhost/addressbook/group.php"

        payload = "group_name=QA_TEST_1313&group_header=&group_footer=&submit=Enter+information"
        headers = {
            'Cookie': 'uin=fb20a53ab67f52a827f791fe3bc1fc8a; uin=fb20a53ab67f52a827f791fe3bc1fc8a',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://localhost/addressbook/group.php?new=New+group',
            'Upgrade-Insecure-Requests': '1'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
