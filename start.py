from  Metatrader_API import MTraderAPI
from  datetime  import datetime as dt,timedelta

api = MTraderAPI()



tim = dt.now()

times = int((tim -timedelta(1)).timestamp())
print(times)

##print(api.construct_and_send(action="CONFIG", symbol="Crash 500 Index", chartTF="M1"))
rep = api.construct_and_send(action="HISTORY", actionType="DATA", symbol="Crash 500 Index", chartTF="M1", fromDate=times)

print(rep) 
