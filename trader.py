##| TRADE     | ORDER_TYPE_BUY        | Buy market                   |
##| TRADE     | ORDER_TYPE_SELL       | Sell market                  |
##| TRADE     | ORDER_TYPE_BUY_LIMIT  | Buy limit                    |
##| TRADE     | ORDER_TYPE_SELL_LIMIT | Sell limit                   |
##| TRADE     | ORDER_TYPE_BUY_STOP   | Buy stop                     |
##| TRADE     | ORDER_TYPE_SELL_STOP  | Sell stop                    |
##| TRADE     | POSITION_MODIFY       | Position modify              |
##| TRADE     | POSITION_PARTIAL      | Position close partial       |
##| TRADE     | POSITION_CLOSE_ID     | Position close by id         |
##| TRADE     | POSITION_CLOSE_SYMBOL | Positions close by symbol    |
##| TRADE     | ORDER_MODIFY          | Order modify                 |
##| TRADE     | ORDER_CANCEL          | Order cancel                 |



import time
from  Metatrader_API import MTraderAPI
api = MTraderAPI()


class trade():
    def get_position(self):
        posit = api.construct_and_send(action="POSITIONS", symbol="Crash 500 Index")
        acc = api.construct_and_send(action="ACCOUNT") 
        return posit,acc
    def open(self):
        rep = api.construct_and_send(action="TRADE", actionType="ORDER_TYPE_BUY", symbol="Crash 500 Index", volume =10)
        print(rep)
        
    def close(self):
        pass
    def calc_profit(self):
        acc = api.construct_and_send(action="ACCOUNT")
        balance =  acc["balance"]
        equity =   acc[""]
        margin = acc[""]
        free_margin = acc[""]
        margin_level = acc[""]
        
         'balance': 10112.08, 'equity': 10048.78, 'margin': 224.59, 'margin_free': 9824.19, 'margin_level': 4474.27757
         
    def modify(self):
        print(self.get_position())
    def main(self):
##        self.open()
        self.modify()

        

if __name__ == "__main__":
    new = trade()
    new.main()    
