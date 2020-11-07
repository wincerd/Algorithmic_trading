import time

import backtrader as bt
from datetime import datetime


class cashier():
    def margin(self):
        marg =  "Up to 1:1000"
        #Total Equity =( Cash + Open Position Profits - Open PositionLosses)
        #Margin Requirement = (Current Price × Units Traded × Margin)
        #Initial Margin =  (price x size) / leverage. 
