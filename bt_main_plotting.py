import datetime
import backtrader as bt

# simple moving average
class SimpleMA(bt.Strategy):
    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(
            self.data, period=20, plotname="20 SMA"
        )


# Instantiate Cerebro engine, disable standard stats
cerebro = bt.Cerebro(stdstats=False)

# Set data parameters and add to Cerebro
data1 = bt.feeds.YahooFinanceCSVData(
    dataname='TSLA.csv',
    fromdate=datetime.datetime(2018, 1, 1),
    todate=datetime.datetime(2020, 1, 1),
)

cerebro.adddata(data1)

''' second data feed
data2 = bt.feeds.YahooFinanceCSVData(
	dataname='AAPL.csv',
	fromdate=datetime.datetime(2018, 1, 1),
	todate=datetime.datetime(2020, 1, 1))

data2.compensate(data1)  #data2 is a dependent of data1
data2.plotinfo.plotmaster = data1
data2.plotinfo.sameaxis = True #prevent plots from converging on final data point

cerebro.adddata(data2)
'''

# Add strategy to show simple moving average on chart
cerebro.addstrategy(SimpleMA)

# Run Cerebro Engine
cerebro.run()
cerebro.plot()


'''
REFERENCE: Plotting options
plotinfo = dict(plot=True,
                subplot=True,
                plotname='',
                plotskip=False,
                plotabove=False,
                plotlinelabels=False,
                plotlinevalues=True,
                plotvaluetags=True,
                plotymargin=0.0,
                plotyhlines=[],
                plotyticks=[],
                plothlines=[],
                plotforce=False,
                plotmaster=None,
                plotylimited=True,
           )
'''
