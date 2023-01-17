import Defs as df
import Users as us
from datetime import date
from datetime import datetime

def NewLog(função,txt):
    now = date.today()
    hour = datetime.today()
    now = f'{now.day}/{now.month}/{now.year} - {hour.hour}:{hour.minute}:{hour.second}'
    # log = open('log.txt','a')
    # log.write('\n'+f'{now:<25}{função:<20}{txt}')
    return True