# calculate SMA10 and SMA30
def add_indicators(df):
    df['SMA10'] = df['Close'].rolling(window=10).mean()
    df['SMA30'] = df['Close'].rolling(window=30).mean()

    return df

# defining the buy/sell signals
def generate_signals(df):
    df['Signal'] = 0
    df.loc[df['SMA10'] > df['SMA30'], 'Signal'] = 1     # buy
    df.loc[df['SMA10'] < df['SMA30'], 'Signal'] = -1    # sell

    return df