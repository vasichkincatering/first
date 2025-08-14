from sqlalchemy import Column, Integer, String, Date

from .database import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_date = Column(Date, nullable=False)
    guests_count = Column(Integer, nullable=False)
    source = Column(String, nullable=True)
    status = Column(String, nullable=True)
