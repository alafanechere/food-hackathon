TCPDUMP_COMMAND = ['sudo', 'tcpdump', '-l', '-I', '-e', '-i', 'en1', '-s', '256', 'type', 'mgt', 'subtype', 'probe-req']
EXCLUDED_MAC = []

EXCLUDED_VENDORS = []
DB_CONNECTION_STRING = "postgresql://user:password@host:5432/hackathon"
