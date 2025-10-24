from ..database import Base
from sqlalchemy import Column, Integer, String, CheckConstraint, DateTime, func




class card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    body = Column(String, nullable=False, unique=True)
    image_path = Column(String, nullable=True, unique=False)
    alternatives = Column(String, nullable=False)
    answer = Column(String(1), nullable=False)
    block = Column(String, nullable=False, unique=False, index=True)
    subject = Column(String, nullable=False, unique=False, index=True)
    espec_subject = Column(String, nullable=False, unique=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    
    __table_args__ = (
        CheckConstraint("answer IN ('a', 'b', 'c', 'd', 'e')"),
        CheckConstraint("block IN ('I', 'II', 'III')"),
    )