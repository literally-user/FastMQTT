import logging
import uuid

import pytest

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture
def topic() -> str:
    return f"/fastmqtt/test/{uuid.uuid4()}"
