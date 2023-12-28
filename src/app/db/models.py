import uuid

from sqlalchemy import Boolean, ForeignKey, Integer, Date
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    title = Column(String, nullable=False)

    users = relationship('User', back_populates='role')


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    father_name = Column(String, nullable=False)
    role_id = Column(ForeignKey('roles.role_id'), nullable=False, default=1)
    is_active = Column(Boolean(), default=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)

    role = relationship('Role', back_populates='users')


class GroupType(Base):
    __tablename__ = "groupTypes"

    groupType_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    title = Column(String, nullable=False)
    customer_amount = Column(Integer(), nullable=False)

    trainersCustomers = relationship('TrainerCustomer', back_populates='groupType')


class TrainerCustomer(Base):
    __tablename__ = "trainersCustomers"

    trainerCustomer_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    trainer_id = Column(ForeignKey('users.user_id'), nullable=False)
    customer_id = Column(ForeignKey('users.user_id'), nullable=False)
    groupType_id = Column(ForeignKey('groupTypes.groupType_id'), nullable=False)

    trainer = relationship('User', back_populates='trainers')
    customer = relationship('User', back_populates='customers')
    groupType = relationship('GroupType', back_populates='groupType')
    trainersCustomers_timetables = relationship('TrainerCustomer_Timetable', back_populates='trainersCustomer')


class Timetable(Base):
    __tablename__ = "timetables"

    timetable_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    workout_date = Column(Date(), nullable=False)
    creation_date = Column(Date(), nullable=False)

    trainersCustomers_timetables = relationship('TrainerCustomer_Timetable', back_populates='timetable')


class TrainerCustomer_Timetable(Base):
    __tablename__ = "trainersCustomers_timetables"

    trainerCustomer_timetable = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    trainerCustomer_id = Column(ForeignKey('trainersCustomers.trainerCustomer_id'), nullable=False)
    timetable_id = Column(ForeignKey('timetables.timetable_id'), nullable=False)

    trainerCustomer = relationship('TrainerCustomer', back_populates='trainersCustomers_timetables')
    timetable = relationship('Timetable', back_populates='trainersCustomers_timetables')
