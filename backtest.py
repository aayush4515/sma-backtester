# the backtest engine
def backtest_strategy(df, initial_cash = 10000):
    cash = initial_cash
    portfolio = []
    holdings = 0

    # if the current signal is buy and the prev signal wasn't buy, buy as much as possible
    # else, sell all the stocks
    # update the portfolio

    for i in range(1, len(df)):
        # buy
        if df['Signal'].iloc[i] == 1 and df['Signal'].iloc[i - 1] != 1:
            holdings = cash / df['Close'].iloc[i]       # buy stocks at last close price
            cash = 0                                    # all cash is spent
        # sell
        elif df['Signal'].iloc[i] == -1 and df['Signal'].iloc[i - 1] != -1:
            cash = holdings * df['Close'].iloc[i]       # sell all stocks
            holdings = 0                                # no stocks left
        # update the portfolio
        total_value = float(cash + (holdings * df['Close'].iloc[i]))
        portfolio.append(total_value)

    # adjust the data frame
    df = df.iloc[1:].copy()                             # skip the first row because there is no signal for comparison
    df['Portfolio Value'] = portfolio                   # add Portfolio column to the data frame

    # return the dataframe
    return df
