import datetime
import sys

TODAY = datetime.datetime.now().date()
NOW = datetime.datetime.now().isoformat(sep="_", timespec="seconds")

class WrongState(Exception):
    pass

def clearing_line():
    sys.stdout.write('\033[A')
    sys.stdout.write('\033[K')
    
    