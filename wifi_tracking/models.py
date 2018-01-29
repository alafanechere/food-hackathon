from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
import config

Base = declarative_base()

class Probe(Base):
    __tablename__ = 'probes'
    # id = Column(Integer, primary_key=True)
    capture_time = Column(DateTime, primary_key=True, index=True)
    mac = Column(String, primary_key=True)
    vendor = Column(String)

    def __repr__(self):
        return "<Probe(mac='%s', capture_time='%s', vendor='%s')>" % (
        self.mac,
        self.capture_time,
        self.vendor)

if __name__ == '__main__':
    engine = create_engine(config.DB_CONNECTION_STRING, echo=True)
    Base.metadata.create_all(engine)
