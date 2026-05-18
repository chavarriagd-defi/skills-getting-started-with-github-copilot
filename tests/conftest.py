from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def reset_activities():
    """Restore in-memory activity data to avoid cross-test contamination."""
    original_activities = deepcopy(app_module.activities)
    app_module.activities = deepcopy(original_activities)
    yield
    app_module.activities = deepcopy(original_activities)


@pytest.fixture
def client(reset_activities):
    return TestClient(app_module.app)
