import uuid

from sqlalchemy import Boolean, ForeignKey, Integer
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

    users = relationship('User', back_populates='role')


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    father_name = Column(String, nullable=False)
    role_id = Column(ForeignKey('roles.role_id'), nullable=False, default=1)
    is_active = Column(Boolean(), default=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)

    role = relationship('Role', back_populates='users')
