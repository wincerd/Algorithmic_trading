import pytz
import backtrader as bt
import backtrader.indicators as btind
from mt5store import MTraderStore
from mt5indicator import getMTraderIndicator
from mt5chart import MTraderChart
from datetime import datetime, timedelta


class SmaCross(bt.SignalStrategy):
    def __init__(self, store):
        self.buy_order = None
        self.live_data = False

        # You can hookup backtrader to any indicator that runs in MT5
        # Attach and retrieve values from the MT5 indicator "Examples/MACD"
        self.mt5macd = getMTraderIndicator(
            # MTraderStorestore instance
            store,
            # Data stream to run the indicator calculations on
            self.datas[0],
            # Set accessor(s) for the indicator output buffers
            ("macd", "signal",),
            # MT5 inidicator name
            indicator="Examples/MACD",
            # Indicator parameters.
            # Any omitted values will use the defaults as defind by the indicator
            params=[12, 26, 9, "PRICE_CLOSE"],
        )()

        # Attach any inidcator to be drawn to a chart window _before_ instantiating the MTraderChart class.
        # self.sma = btind.SimpleMovingAverage(self.data)
        self.bb = btind.BollingerBands(self.data)

        # Open a new chart window in MT5 with symbol and timeframe provided by the passed data stream object.
        # Important: instantiate a new chart with class MTraderChart only after you attached any
        # indicator you want to plot by calling getMTraderIndicator as shown on line 17 above. Otherwise it will fail!
        chart = MTraderChart(data_obj=self.datas[0])

        # Plot the backtrader BollingerBand indicator to a chart window in MT5.
        chart.addline(
            self.bb.top,
            style={
                "shortname": "BT-BollingerBands",
                "linelabel": "Top",
                "color": "clrBlue",
            },
        )
        chart.addline(
            self.bb.mid,
            style={
                "shortname": "BT-BollingerBands",
                "linelabel": "Middle",
                "color": "clrYellow",
            },
        )
        chart.addline(
            self.bb.bot,
            style={
                "shortname": "BT-BollingerBands",
                "linelabel": "Bottom",
                "color": "clrGreen",
            },
        )

    def next(self):
        if self.buy_order is None:
            self.buy_order = self.buy_bracket(
                limitprice=1.13, stopprice=1.10, size=0.1, exectype=bt.Order.Market
            )

        if self.live_data:
            cash = self.broker.getcash()

            # Cancel order
            if self.buy_order is not None:
                self.cancel(self.buy_order[0])

        else:
            # Avoid checking the balance during a backfill. Otherwise, it will
            # Slow things down.
            cash = "NA"

        for data in self.datas:
            print(
                f"{data.datetime.datetime()} - {data._name} | Cash {cash} | O: {data.open[0]} H: {data.high[0]} L: {data.low[0]} C: {data.close[0]} V:{data.volume[0]}"
            )
            print(
                f"MT5 indicator Examples/MACD: {self.mt5macd.signal[0]} {self.mt5macd.macd[0]}"
            )

    def notify_data(self, data, status, *args, **kwargs):
        dn = data._name
        dt = datetime.now()
        msg = f"Data Status: {data._getstatusname(status)}"
        print(dt, dn, msg)
        if data._getstatusname(status) == "LIVE":
            self.live_data = True
        else:
            self.live_data = False


host = "192.168.1.101"

cerebro = bt.Cerebro()
store = MTraderStore(host=host, debug=False, datatimeout=10)
cerebro.addstrategy(SmaCross, store)

# uncomment next 2 lines to use backbroker for live trading with MTraderStore
# broker = store.getbroker(use_positions=True)
# cerebro.setbroker(broker)

start_date = datetime.now() - timedelta(minutes=200)

data = store.getdata(
    dataname="EURUSD",
    timeframe=bt.TimeFrame.Minutes,
    fromdate=start_date,
    compression=1,
    # You need to provide the correct time zone for drawing indicators to charts widows in MT5 to work properly
    tz=pytz.timezone("Europe/Berlin"),
    # useask=True, # Ask price instead if the default bid price
    # addspread=True, # Add the spread value
    historical=True,
)

cerebro.adddata(data)

cerebro.run(stdstats=False)
