from fastapi.testclient import TestClient
from app.main import app

import uuid


def get_token():
    username = f"user_{uuid.uuid4().hex[:8]}"

    client.post(
        "/auth/register",
        json={
            "username": username,
            "password": "Password@123"
        }
    )

    response = client.post(
        "/auth/token",
        data={
            "username": username,
            "password": "Password@123"
        }
    )

    return response.json()["access_token"]

client = TestClient(app)


import uuid

def test_register_user_success():

    username = f"user_{uuid.uuid4().hex[:8]}"

    response = client.post(
        "/auth/register",
        json={
            "username": username,
            "password": "Password@123"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["username"] == username
    assert "id" in data

def test_register_duplicate_username():

    client.post(
        "/auth/register",
        json={
            "username": "duplicateuser",
            "password": "Password@123"
        }
    )

    response = client.post(
        "/auth/register",
        json={
            "username": "duplicateuser",
            "password": "Password@123"
        }
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "Username already exists"


def test_register_invalid_password():

    response = client.post(
        "/auth/register",
        json={
            "username": "weakpassword",
            "password": "password"
        }
    )

    assert response.status_code == 422


def test_register_short_username():

    response = client.post(
        "/auth/register",
        json={
            "username": "ab",
            "password": "Password@123"
        }
    )

    assert response.status_code == 422


def test_login_success():

    client.post(
        "/auth/register",
        json={
            "username": "loginuser",
            "password": "Password@123"
        }
    )

    response = client.post(
        "/auth/token",
        data={
            "username": "loginuser",
            "password": "Password@123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password():

    client.post(
        "/auth/register",
        json={
            "username": "wrongpassuser",
            "password": "Password@123"
        }
    )

    response = client.post(
        "/auth/token",
        data={
            "username": "wrongpassuser",
            "password": "WrongPassword@123"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password"


def test_login_unknown_user():

    response = client.post(
        "/auth/token",
        data={
            "username": "nouser",
            "password": "Password@123"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password"


def test_password_without_uppercase():

    response = client.post(
        "/auth/register",
        json={
            "username": f"user_{uuid.uuid4().hex[:8]}",
            "password": "password@123"
        }
    )

    assert response.status_code == 422


def test_password_without_lowercase():

    response = client.post(
        "/auth/register",
        json={
            "username": f"user_{uuid.uuid4().hex[:8]}",
            "password": "PASSWORD@123"
        }
    )

    assert response.status_code == 422


def test_password_without_digit():

    response = client.post(
        "/auth/register",
        json={
            "username": f"user_{uuid.uuid4().hex[:8]}",
            "password": "Password@"
        }
    )

    assert response.status_code == 422    

def test_register_without_special_character():

    response = client.post(
        "/auth/register",
        json={
            "username": "nospecial123",
            "password": "Password123"
        }
    )

    assert response.status_code == 422    