import zmq
import threading
import queue
from  Metatrader_API import MTraderAPI
from  datetime  import datetime as dt,timedelta
from queue import Queue
from threading import Thread
import time
import pandas as pd 
pd.options.plotting.backend = "matplotlib"
import matplotlib.pyplot as plt
api = MTraderAPI()
class Streamer():
    row = 1
    def __init__(self,symbl,Tf):
        api.construct_and_send(action="CONFIG",
                                     symbol= symbl, chartTF=Tf)
    def parse(self,data):
        data = data["data"]
        
##        a = pd.columns["time","open","close"]
        
        a = pd.DataFrame({"time":[data[0]],"open":[data[1]],"close":[data[2]]},index= [self.row])
        
        
        
        
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
            
            
    def main(self):
        t = threading.Thread(target=self._t_livedata, daemon=True)
        t.start()
        t = threading.Thread(target=self._t_streaming_events, daemon=True)
        t.start()        
            
if __name__ == "__main__":
    new = Streamer("Crash 500 Index","TICK")
    new.main()



