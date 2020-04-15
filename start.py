from  Metatrader_API import MTraderAPI
from  datetime  import datetime as dt,timedelta

api = MTraderAPI()


class Trader():
    def __ini__():
        pass
         
    
    def time(self):
        '''
        :return current time in epoch
        :param candles_2rows_dataframe: dataframe that consists of two rows of candles in chronological order, created by get_num_rows(self, n)
        '''
        tim = int((dt.now()).timestamp())
        
##        times = int((tim -timedelta(1)).timestamp())
        
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
    
