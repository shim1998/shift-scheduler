from datetime import datetime
from fetchdata import FetchData

def getrownumber(hour,date):
    row=(hour//2)+3+(12 if date%2==0 else 0)
    return row

time = datetime.today()
hour = time.hour
date = time.day
row = getrownumber(16,14)
data = FetchData()
Responders = data.getdata(RANGE='C'+str(row))
Verifiers = data.getdata(RANGE='D'+str(row))
Researchers = data.getdata(RANGE='E'+str(row))
print(Responders)
print(Verifiers)
print(Researchers)