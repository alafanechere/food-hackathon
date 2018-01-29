import subprocess as sub
import datetime
from pytz import timezone
import pytz
import pprint
import manuf

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Probe
import config

Base = declarative_base()
engine = create_engine(config.DB_CONNECTION_STRING, echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


pp = pprint.PrettyPrinter(indent=2)
manuf_parser = manuf.MacParser()
CURRENT_TZ = timezone('Europe/Paris')

def probe_handler(probe):
    manuf_lookup = manuf_parser.get_all(probe['mac'])
    probe['vendor'] = manuf_lookup.manuf_long

    if probe['mac'] not in config.EXCLUDED_MAC and probe['vendor'] not in config.EXCLUDED_VENDORS and manuf_lookup.manuf_long is not None :
        insert_probe(probe)

def capture(iface_name='en1', tcpdump_cmd=config.TCPDUMP_COMMAND, probe_handler=probe_handler):
    tcpdump_cmd[6] = iface_name
    p = sub.Popen(tcpdump_cmd, stdout=sub.PIPE)

    for row in iter(p.stdout.readline, b''):
        split = row.decode('utf-8').split(' ')
        capture_time = datetime.datetime.strptime(split[0], '%H:%M:%S.%f', )
        now = datetime.datetime.now()
        capture_time = capture_time.replace(year=now.year, month=now.month, day=now.day)
        capture_time = CURRENT_TZ.localize(capture_time)
        try:
            mac = [s for s in split if s.startswith('SA')][0].replace('SA:', '')
            probe_handler({'mac': mac, 'capture_time': capture_time})
        except:
            pass

def insert_probe(enriched_probe):
    new_probe = Probe(mac=enriched_probe['mac'],
                        capture_time=enriched_probe['capture_time'],
                        vendor=enriched_probe['vendor'])
    session.add(new_probe)
    session.commit()
    print('insert')

if __name__ == '__main__':
    capture()
