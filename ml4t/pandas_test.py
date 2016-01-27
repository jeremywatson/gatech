import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_selected(df, columns, start_index, end_index):
    plot_data(df.ix[start_index:end_index, columns])

def plot_data(df, title="Stock prices"):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def normalize_data(df):
	return df / df.ix[0,:]

def compute_daily_returns(df):
	daily_returns = df.copy()
	daily_returns[1:] = (df[1:] / df[:-1].values) - 1

	# we can also use pandas shift
	# daily_returns = (df / df.shift(1)) - 1

	daily_returns.ix[0, :] = 0

	return daily_returns

def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=["SPY"])

    return df

def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']  # SPY will be added in get_data()
    
    # Get stock data
    df = get_data(symbols, dates)

    # compute statistics
    print df.mean() # prints mean for each column
    print df.median()
    print df.std()

    # rolling mean for GOOG
    goog_plot = df['GOOG'].plot(title='GOOG rolling mean', label='GOOG')
    rm_goog = pd.rolling_mean(df['GOOG'], window=20)
    rm_goog.plot(label='rolling mean', ax=goog_plot)
    goog_plot.legend(loc='upper left')
    plt.show()


if __name__ == "__main__":
    test_run()