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
        posit = api.construct_and_send(action="POSITIONS")
        return posit
    def open(self,volume):
        rep = api.construct_and_send(action="TRADE", actionType="ORDER_TYPE_BUY", symbol="Crash 500 Index", volume =volume)
        print("tick",rep)
        
    def close(self,symbol):
        rep = api.construct_and_send(action="TRADE", actionType="POSITION_CLOSE_SYMBOL", symbol="Crash 500 Index")
        print(rep)
    def positions_in_profit(self):
        positions = self.get_position()
        a,p = positions
        for i in positions[p]:
            print(i)
    def calc_profit(self):
        acc = api.construct_and_send(action="ACCOUNT")
        balance =  acc["balance"]
        equity =   acc["equity"]
        margin = acc["margin"]
        free_margin = acc["margin_free"]
        margin_level = acc["margin_level"]
    def modify(self,volume):
        positions = self.get_position()
        a,p = positions
        for i in positions[p]:
            a = api.construct_and_send(action="TRADE", actionType="POSITION_PARTIAL", symbol="Crash 500 Index", volume = volume ,id= i["id"])
            print(a)
    def main(self):
        self.open(1)
        print(self.get_position())
        time.sleep(10)
        self.positions_in_profit()
        self.modify(0.40)
        time.sleep(15)
        self.modify(0.30)
        time.sleep(20)
        self.modify(0.10)
        time.sleep(18)
        self.modify(0.10)
        time.sleep(18)
        self.close("Crash 500 Index")

if __name__ == "__main__":
    new = trade()
    new.main()    
