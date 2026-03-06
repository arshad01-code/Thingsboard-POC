from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    tb_customer_id = Column(String, nullable=False)
    devices = relationship("Device", back_populates="customer")

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, default="default")
    tb_device_id = Column(String, nullable=False)
    device_token = Column(String, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    customer = relationship("Customer", back_populates="devices")

class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    temperature = Column(Float)
    humidity = Column(Float)
    pressure = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Alert(Base):

    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    alert_type = Column(String)
    severity = Column(String)
    message = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Rule(Base):

    __tablename__ = "rules"

    id = Column(Integer, primary_key=True)
    metric = Column(String)
    operator = Column(String)
    threshold = Column(Float)
    alert_message = Column(String)
