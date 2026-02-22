from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    tb_customer_id = Column(String, unique=True)
   
class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    tb_device_id = Column(String, unique=True)
    tb_device_token = Column(String)

class CustomerDevice(Base):
    __tablename__ = "customer_devices"

    id = Column(Integer, primary_key=True)
    customer_id = Column(String, ForeignKey("customers.id", ondelete="CASCADE"))
    device_id = Column(String, ForeignKey("devices.id", ondelete="CASCADE"))
