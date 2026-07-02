# Present so pytest adds this project directory to sys.path, which lets the
# tests import the application package with `from app.main import app`
# regardless of how pytest is invoked.

import os
import tempfile

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine

from app.database import get_session
from app.main import app


db_fd, db_path = tempfile.mkstemp()

engine = create_engine(
    f"sqlite:///{db_path}",
    connect_args={"check_same_thread": False}
)

SQLModel.metadata.create_all(engine)


def override_get_session():
    with Session(engine) as session:
        yield session


app.dependency_overrides[get_session] = override_get_session


@pytest.fixture
def client():
    return TestClient(app)


