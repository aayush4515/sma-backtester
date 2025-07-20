# load data from yahoo finance
import matplotlib.pyplot as plt
import yfinance as yf
import strategy as st
import backtest as bt


initial_cash = input("Enter the cash to begin with: ")
ticker = input("Enter the stock you want to analyze\nOptions are: AAPL, MSFT, TSLA, GOOGL, AMZN, NVDA, JPM, BAC, TSLA, XOM, JNJ: ")

# create a data frame
df = yf.download(ticker, start='2021-01-01', end='2025-01-01')

# add indicators
df = st.add_indicators(df)

# generate buy/sell signals
df = st.generate_signals(df)

# run the backtesting strategy
df = bt.backtest_strategy(df, initial_cash)

# check the strategy
print(df.tail(30))

# plot SMAs and portfolio values over price
df.plot(y = ['Portfolio Value'])
plt.show()
