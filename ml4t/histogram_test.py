import pandas as pd
import matplotlib.pyplot as plt

from util import get_data, plot_data

def compute_daily_returns(df):
	daily_returns = df.copy()
	daily_returns[1:] = (df[1:] / df[:-1].values) - 1
	daily_returns.ix[0,:] = 0
	return daily_returns

def main():
	dates = pd.date_range('2009-01-01', '2012-12-31')
	symbols = ['SPY']
	df = get_data(symbols, dates)
	plot_data(df)

	daily_returns = compute_daily_returns(df)

	# histogram
	daily_returns.hist(bins=20)
	
	'''	
	call this twice if wanting to plot 2+ charts on same chart:
	daily_returns['SPY'].hist(bins=20, label="SPY")
	daily_returns['XOM'].hist(bins=20, label="XOM")
	'''

	mean = daily_returns['SPY'].mean()
	std = daily_returns['SPY'].std()

	plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
	plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
	plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
	plt.show()

	print daily_returns.kurtosis()


if __name__ == '__main__':
	main()