from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class FutureMessage(Base):
    __tablename__ = "future_messages"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)


class GrowthEntry(Base):
    __tablename__ = "growth_entries"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    progress = Column(Integer, nullable=False)
