import datetime
import backtrader as bt
from strategies import *

# Instantiate Cerebro engine
cerebro = bt.Cerebro()

# Add CSV data for all tickers to Cerebro
instruments = ['TSLA', 'AAPL', 'GE', 'GRPN']
for ticker in instruments:
	data = bt.feeds.YahooFinanceCSVData(
		dataname='{}.csv'.format(ticker),
		fromdate=datetime.datetime(2016, 1, 1),
		todate=datetime.datetime(2017, 10, 30),
	)
	cerebro.adddata(data)

# Add analyzer for screener
cerebro.addanalyzer(Screener_SMA)

if __name__ == '__main__':
	# Run Cerebro Engine
	cerebro.run(runonce=False, stdstats=False, writer=True)
