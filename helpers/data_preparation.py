from helpers.api.group_api import GroupApi
from faker import Faker

from helpers.dto_group import Group
from test_add_group import TestAddGroup as AddGroup

fake = Faker()


class PreparationGroup:

    @staticmethod
    def preparation_group_api(base_url: str) -> str:
        prefix_add_group = f"{base_url}group.php"
        group_name = f"New_{fake.isbn13(separator='-')}"
        payload_add_group = f"group_name={group_name}&group_header=&group_footer=&submit=Enter+information"
        GroupApi.create_group(prefix=prefix_add_group, payload=payload_add_group)
        return group_name

    @staticmethod
    def preparation_group_ui(wd) -> str:
        group_name = f"New_{fake.isbn13(separator='-')}"
        AddGroup.open_group_page(wd)
        AddGroup.create_group(wd=wd, group=Group(name=f"{group_name}", header="1", footer="2"))
        return group_name
