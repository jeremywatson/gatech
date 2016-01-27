import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from util import get_data, plot_data

def compute_daily_returns(df):
	daily_returns = df.copy()
	daily_returns[1:] = (df[1:] / df[:-1].values) - 1
	daily_returns.ix[0,:] = 0
	return daily_returns

def main():
	dates = pd.date_range('2009-01-01', '2012-12-31')
	symbols = ['SPY', 'XOM', 'GLD']
	df = get_data(symbols, dates)
	plot_data(df)

	daily_returns = compute_daily_returns(df)

	daily_returns.plot(kind='scatter', x='SPY', y='XOM')
	beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)

	plt.show()

	daily_returns.plot(kind='scatter', x='SPY', y='GLD')
	plt.show()


if __name__ == '__main__':
	main()