import zmq
import threading
from  Metatrader_API import MTraderAPI
from  datetime  import datetime as dt,timedelta




api = MTraderAPI()



tim = dt.now()

times = int((tim -timedelta(1)).timestamp())
print(times)
##print(api.construct_and_send(action="CONFIG", symbol="Crash 500 Index", chartTF="M1"))
rep = api.construct_and_send(action="HISTORY", actionType="DATA", symbol="Crash 500 Index", chartTF="M1", fromDate=times)
print(rep)
print(api.construct_and_send(action="CONFIG", symbol="Crash 500 Index", chartTF="M1"))

def _t_livedata():
    socket = api.live_socket()
    while True:
        try:
            last_candle = socket.recv_json()
            print(last_candle)
        except zmq.ZMQError:
            raise zmq.NotDone("Live data ERROR")
        print(last_candle)


def _t_streaming_events():
    socket = api.streaming_socket()
    while True:
        try:
            trans = socket.recv_json()
            request, reply = trans.values()
        except zmq.ZMQError:
            raise zmq.NotDone("Streaming data ERROR")
        print(request)
        print(reply)



t = threading.Thread(target=_t_livedata, daemon=True)
t.start()

t = threading.Thread(target=_t_streaming_events, daemon=True)
t.start()

while True:
    pass
