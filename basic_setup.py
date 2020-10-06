import datetime
import backtrader as bt
from strategy import MyStrategy


class MyStrategy(bt.Strategy):
    def next(self):
        print(self.datas[0].close[0])  # Print close prices


# Instantiate Cerebro engine
cerebro = bt.Cerebro()

# Set data parameters and add to Cerebro
data = bt.feeds.YahooFinanceCSVData(
    dataname='TSLA.csv',
    fromdate=datetime.datetime(2016, 1, 1),
    todate=datetime.datetime(2016, 12, 31),
)

cerebro.adddata(data)

# Add strategy to Cerebro
cerebro.addstrategy(MyStrategy)

# Run Cerebro Engine
cerebro.run()
