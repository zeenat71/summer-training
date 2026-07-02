from sqlmodel import Session, create_engine
from app.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

def get_session():
    with Session(engine) as session:
        yield session