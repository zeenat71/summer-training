from app.auth import create_access_token
from fastapi.testclient import TestClient
from app.main import app

import uuid

client = TestClient(app)


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


def auth_header():

    token = get_token()

    return {
        "Authorization": f"Bearer {token}"
    }


def create_patient():

    response = client.post(
        "/patients",
        headers=auth_header(),
        json={
            "name": "Ali",
            "age": 25,
            "condition": "Flu",
            "risk_score": 30,
            "active": True
        }
    )

    return response.json()["id"]


def test_get_patients():

    response = client.get("/patients")

    assert response.status_code == 200


def test_create_patient():

    response = client.post(
        "/patients",
        headers=auth_header(),
        json={
            "name": "Ahmed",
            "age": 40,
            "condition": "Fever",
            "risk_score": 50,
            "active": True
        }
    )

    assert response.status_code == 201


def test_create_patient_without_token():

    response = client.post(
        "/patients",
        json={
            "name": "Ahmed",
            "age": 40,
            "condition": "Fever",
            "risk_score": 50,
            "active": True
        }
    )

    assert response.status_code == 401


def test_get_patient_by_id():

    patient_id = create_patient()

    response = client.get(f"/patients/{patient_id}")

    assert response.status_code == 200


def test_get_patient_not_found():

    response = client.get("/patients/999999")

    assert response.status_code == 404


def test_put_patient():

    patient_id = create_patient()

    response = client.put(
        f"/patients/{patient_id}",
        headers=auth_header(),
        json={
            "name": "Updated",
            "age": 60,
            "condition": "Diabetes",
            "risk_score": 80,
            "active": False
        }
    )

    assert response.status_code == 200


def test_put_patient_not_found():

    response = client.put(
        "/patients/999999",
        headers=auth_header(),
        json={
            "name": "Updated",
            "age": 60,
            "condition": "Diabetes",
            "risk_score": 80,
            "active": False
        }
    )

    assert response.status_code == 404


def test_patch_patient():

    patient_id = create_patient()

    response = client.patch(
        f"/patients/{patient_id}",
        headers=auth_header(),
        json={
            "risk_score": 99
        }
    )

    assert response.status_code == 200


def test_patch_not_found():

    response = client.patch(
        "/patients/999999",
        headers=auth_header(),
        json={
            "risk_score": 99
        }
    )

    assert response.status_code == 404


def test_delete_patient():

    patient_id = create_patient()

    response = client.delete(
        f"/patients/{patient_id}",
        headers=auth_header()
    )

    assert response.status_code == 204


def test_delete_not_found():

    response = client.delete(
        "/patients/999999",
        headers=auth_header()
    )

    assert response.status_code == 404


def test_invalid_age():

    response = client.post(
        "/patients",
        headers=auth_header(),
        json={
            "name": "Ali",
            "age": 150,
            "condition": "Flu",
            "risk_score": 20,
            "active": True
        }
    )

    assert response.status_code == 422


def test_invalid_risk_score():

    response = client.post(
        "/patients",
        headers=auth_header(),
        json={
            "name": "Ali",
            "age": 20,
            "condition": "Flu",
            "risk_score": 120,
            "active": True
        }
    )

    assert response.status_code == 422

def test_filter_active():

    response = client.get("/patients?active=true")

    assert response.status_code == 200


def test_filter_condition():

    response = client.get("/patients?condition=Flu")

    assert response.status_code == 200    


def test_invalid_token():

    response = client.post(
        "/patients",
        headers={
            "Authorization": "Bearer invalidtoken123"
        },
        json={
            "name": "Ali",
            "age": 20,
            "condition": "Flu",
            "risk_score": 20,
            "active": True
        }
    )

    assert response.status_code == 401    


def test_token_without_sub():
    token = create_access_token({})

    response = client.post(
        "/patients",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Ali",
            "age": 20,
            "condition": "Flu",
            "risk_score": 20,
            "active": True,
        },
    )

    assert response.status_code == 401


from app.auth import create_access_token
from app.database import engine
from sqlmodel import Session
from app.models import User

from app.database import get_session


client = TestClient(app)

def test_invalid_token_without_sub():
    token = create_access_token({})

    response = client.post(
        "/patients",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Ali",
            "age": 20,
            "condition": "Flu",
            "risk_score": 10,
            "active": True
        }
    )

    assert response.status_code == 401


def test_get_session_generator():
    session_gen = get_session()
    session = next(session_gen)

    assert session is not None

    session.close()

