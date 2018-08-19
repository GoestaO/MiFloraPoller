from sqlalchemy import Column, Integer, DateTime, Float, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import datetime

Base = declarative_base()


class SensorData(Base):
    __tablename__ = 'sensordata'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    sensor_name = Column(String(50))
    temperature = Column(Float)
    moisture = Column(Integer)
    fertility = Column(Integer)
    light = Column(Integer)
    battery = Column(Integer)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<Sensor: {4}, Timestamp: {0}; temperature: {1}; moisture: {2}; fertility: {3}>'.format(self.timestamp,
                                                                                                       self.temperature,
                                                                                                       self.moisture,
                                                                                                       self.fertility,
                                                                                                       self.sensor_name)
