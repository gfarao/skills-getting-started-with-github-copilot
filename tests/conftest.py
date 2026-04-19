from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    # Keep tests independent because endpoint calls mutate in-memory state.
    snapshot = deepcopy(activities)
    try:
        yield
    finally:
        activities.clear()
        activities.update(snapshot)
