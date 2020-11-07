import zmq
import threading
import queue
from  Metatrader_API import MTraderAPI
from datetime import datetime as dt , timedelta
from queue import Queue
from threading import Thread
import time
import pandas as pd 
pd.options.plotting.backend = "plotly"
from trader import trade

import datetime

api = MTraderAPI()
class Streamer():
    row = 1
    def __init__(self,symbl,Tf):
        api.construct_and_send(action="CONFIG",
                                     symbol= symbl, chartTF=Tf)
    def parse(self,data):
        data = data["data"]
        
##        a = pd.columns["time","open","close"]
        print(data)
        a = pd.DataFrame({"time":[data[0]],"open":[data[1]],"close":[data[4]]},index= [self.row])
        self.row += 1
        if (data[1] > data[4]):
           print("trade",a)
           new = trade()
           new.open()
           current_time = (( data[0] //60) * 60 )
           utc_time = dt.utcfromtimestamp(current_time)
           future = utc_time + datetime.timedelta(minute=1)
           time.sleep((future).seconds)
           print(utc_time,future)
           syb = new.get_position()['positions']['symbol']   
           new.close(syb)
        else:
           print(data[1] > data[2])
           print(a)

    def _t_livedata(self):
        socket = api.live_socket()
        while True:
            try:
                last_candle = socket.recv_json()
            except zmq.ZMQError:
                raise zmq.NotDone("Live data ERROR")
            self.parse(last_candle)
    def _t_streaming_events(self):
        socket = api.streaming_socket()
        while True:
            try:
                trans = socket.recv_json()
                request, reply = trans.values()
            except zmq.ZMQError:
                raise zmq.NotDone("Streaming data ERROR")
    def reset(self):
        rep = api.construct_and_send(action="RESET")
        print(rep)
    def main(self):
        t = threading.Thread(target=self._t_livedata, daemon=True)
        t.start()
        t = threading.Thread(target=self._t_streaming_events, daemon=True)
        t.start()        
            
if __name__ == "__main__":
    new = Streamer("Crash 500 Index","M1")
    new.main()



