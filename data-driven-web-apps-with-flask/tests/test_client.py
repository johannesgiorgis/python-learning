import pytest

import sys
import os

container_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, container_folder)

import pypi_org.app
from pypi_org.app import app as flask_app


@pytest.fixture
def client():
    flask_app.app.config["TESTING"] = True
    client = flask_app.app.test_client()

    # noinspection PyBroadException,PyUnusedLocal
    try:
        flask_app.register_blueprint()
    except:
        pass

    flask_app.init_db()
    # client.post()

    yield client
