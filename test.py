import zmq
import threading
from  Metatrader_API import MTraderAPI

api = MTraderAPI()
symbl = "Crash 500 Index"
Tf = "tick"
api.construct_and_send(action="CONFIG",
                                     symbol= symbl, chartTF=Tf)
def _t_livedata():
    socket = api.live_socket()
    while True:
        try:
            last_candle = socket.recv_json()
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
