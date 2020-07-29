from  Metatrader_API import MTraderAPI
import threading
import queue
from  datetime  import datetime as dt,timedelta
from stream import Streamer


api = MTraderAPI()
my_queue = queue.Queue()

Streamer("Crash 500 Index","1mn")

def storeInQueue(f):
  def wrapper(*args):
    my_queue.put(f(*args))
  return wrapper


class Trader():
    def __ini__():
        pass
         
    
    def time(self):
        '''
        :return current time in epoch
        :param candles_2rows_dataframe: dataframe that consists of two rows of candles in chronological order, created by get_num_rows(self, n)
        '''
        tim = int((dt.now()).timestamp())
        return tim
    def signal(self):
        pass 

    def current_price(self):
        pass
        
    def trade(self,typ,volum,symbl):
        if typ == "sell":
            api.construct_and_send(action="TRADE", actionType="ORDER_TYPE_SELL",
                                   symbol=symbl, volume=volum, stoploss=1.1, takeprofit=1.3)
        elif typ == "Buy":
            api.construct_and_send(action="TRADE", actionType="ORDER_TYPE_BUY",
                                   symbol=symbl,volume =volum, stoploss=1.1, takeprofit=1.3)
    def main(self):
        self.time()
     
        
          
 
    
if __name__ == "__main__":
    new = Trader()
    new.main()
    
