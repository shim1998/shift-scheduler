import json
from datetime import datetime
from fetchdata import FetchData
class Fetch:
    def getrownumber(self,hour,date):
        row=(hour//2)+3+(12 if date%2==0 else 0)
        return row
        
    def return_data(self):
        time = datetime.today()
        hour = time.hour
        date = time.day
        row = self.getrownumber(hour,date)
        data = FetchData()
        Responders = data.getdata(RANGE='C'+str(row))
        Verifiers = data.getdata(RANGE='D'+str(row))
        Researchers = data.getdata(RANGE='E'+str(row))
        Responders_List=str(Responders[0][0]).split(',')
        Verifiers_List=str(Verifiers[0][0]).split(',')
        Researchers_List=str(Researchers[0][0]).split(',')
        return Responders_List+Verifiers_List+Researchers_List
