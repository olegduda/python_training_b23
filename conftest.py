import importlib

import jsonpickle
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


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            test_data = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        if fixture.startswith("json_"):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_module(module):
    return importlib.import_module(f'data.{module}').test_data


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data\\{file}.json")) as file:
        return jsonpickle.decode(file.read())
