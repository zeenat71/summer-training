from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import (
    Patient,
    PatientCreate,
    PatientRead,
    PatientUpdate,
    User,
)
from app.auth import get_current_user

router = APIRouter(tags=["Patients"])


# ---GET ALL PATIENTS----


@router.get(
    "/patients",
    response_model=list[PatientRead],
    status_code=status.HTTP_200_OK,
    summary="Get all patients"
)
def get_all_patients(
    session: Session = Depends(get_session),
    active: Optional[bool] = None,
    condition: Optional[str] = None,
    limit: int = 30,
    offset: int = 0,
):

    filtered_patients = session.exec(select(Patient)).all()

    if active is not None:
        temp = []
        for patient in filtered_patients:
            if patient.active == active:
                temp.append(patient)
        filtered_patients = temp

    if condition is not None:
        temp = []
        for patient in filtered_patients:
            if patient.condition.lower() == condition.lower():
                temp.append(patient)
        filtered_patients = temp

    return filtered_patients[offset: offset + limit]


# --- GET PATIENT BY ID ---


@router.get(
    "/patients/{id}",
    response_model=PatientRead,
    status_code=status.HTTP_200_OK,
    summary="Get patient by id"
)
def get_patient_byId(
    id: int,
    session: Session = Depends(get_session)
):

    patient = session.get(Patient, id)

    if patient:
        return patient

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Patient not found"
    )


# ---CREATE PATIENT---


@router.post(
    "/patients",
    response_model=PatientRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create patient"
)
def create_patient(
    patient: PatientCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):

    new_patient = Patient.model_validate(patient)

    session.add(new_patient)
    session.commit()
    session.refresh(new_patient)

    return new_patient


# --- UPDATE Patient --- (PUT)


@router.put(
    "/patients/{id}",
    response_model=PatientRead,
    status_code=status.HTTP_200_OK,
    summary="Update patient"
)
def update_patient(
    id: int,
    patient: PatientCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):

    patient_data = session.get(Patient, id)

    if patient_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    patient_data.name = patient.name
    patient_data.age = patient.age
    patient_data.condition = patient.condition
    patient_data.risk_score = patient.risk_score
    patient_data.active = patient.active

    session.add(patient_data)
    session.commit()
    session.refresh(patient_data)

    return patient_data


# ---UPDATE PATIENT--- (PATCH)


@router.patch(
    "/patients/{id}",
    response_model=PatientRead,
    status_code=status.HTTP_200_OK,
    summary="Partially update patient"
)
def partial_update_patient(
    id: int,
    patient: PatientUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):

    patient_record = session.get(Patient, id)

    if patient_record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    update_data = patient.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(patient_record, key, value)

    session.add(patient_record)
    session.commit()
    session.refresh(patient_record)

    return patient_record


# DELETE Patient


@router.delete(
    "/patients/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete patient"
)
def delete_patient(
    id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):

    patient = session.get(Patient, id)

    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    session.delete(patient)
    session.commit()

    return