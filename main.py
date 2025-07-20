# load data from yahoo finance
import matplotlib.pyplot as plt
import yfinance as yf
import strategy as st
import backtest as bt

# create a data frame
df = yf.download('MSFT', start='2021-01-01', end='2023-01-01')

# add indicators
df = st.add_indicators(df)

# generate buy/sell signals
df = st.generate_signals(df)

# run the backtesting strategy
df = bt.backtest_strategy(df)

# check the strategy
print(df.tail(30))

# plot SMAs and portfolio values over price
df.plot(y = ['Portfolio Value'])
plt.show()
