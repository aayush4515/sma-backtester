# total returns over the time period
def total_return(initial_cash, df):
    closing_value = df['Portfolio Value'].iloc[len(df) - 1]
    return closing_value - initial_cash

# calculate max drawdown
def calculate_max_drawdown(df):
    # extract portfolio value over time in a list
    portfolio = df['Portfolio Value'].tolist()


    # calculate max drawdown
    peak = portfolio[0]
    max_drawdown = 0

    for value in portfolio:
        if value > peak:
            peak = value
        curr_drawdown = (value - peak) / peak
        max_drawdown = min(max_drawdown, curr_drawdown)

    # return as a percent
    return max_drawdown * 100