from email.policy import default
from sqlalchemy import Boolean, PrimaryKeyConstraint, String, Integer, Column

from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    complete = Column(Boolean, default=False)