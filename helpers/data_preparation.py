from helpers.api.group_api import GroupApi
from helpers.api.auth import AuthApi
from faker import Faker

from model.dto_group import Group

fake = Faker()


class PreparationGroup:

    @staticmethod
    def preparation_group_api(base_url: str, username="admin", password="secret") -> str:
        cookie = AuthApi.auth_user(base_url, username, password)
        group_name = f"New_{fake.isbn13(separator='-')}"
        payload_add_group = f"group_name={group_name}&group_header=&group_footer=&submit=Enter+information"
        GroupApi.create_group(prefix=base_url, payload=payload_add_group, cookie=cookie)
        return group_name

    @staticmethod
    def preparation_group_ui(app) -> str:
        group_name = f"New_{fake.isbn13(separator='-')}"
        app.open_group_page()
        app.create_group(group=Group(name=f"{group_name}", header="1", footer="2"))
        return group_name
