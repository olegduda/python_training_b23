import pytest
import json
import os.path
from fixture.application import Application
from typing import Optional

fixture: Optional[Application] = None
env = None


@pytest.fixture()
def app(request):
    global fixture
    global env

    browser = request.config.getoption("--browser")
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("env"))
    if env is None:
        with open(config_file) as f:
            env = json.load(f)

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=env["base_url"])

    fixture.session.ensure_login(username=env["username"], password=env["password"])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop_session(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--env", action="store", default="env.json")

