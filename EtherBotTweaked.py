import ccxt
import time
import pandas as pd

# Instantiate the Coinbase exchange object
exchange = ccxt.coinbase()

def bot():
    # Set the ticker symbol for Ether
    symbol = 'ETH/USD'

    # Set the length of the moving averages
    short_ma_length = 200
    long_ma_length = 200

    # Set the holding period (in days)
    holding_period = 5

    # Initialize the position variable
    position = None

while True:
    # Get the OHLCV data for the past month
    ohlcv = exchange.fetch_ohlcv(symbol, period='1M')

    # Convert the data to a Pandas data frame
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

    # Calculate the moving averages
    df['short_ma'] = df['close'].rolling(window=200, min_periods=1).mean()
    df['long_ma'] = df['close'].rolling(window=200, min_periods=1).mean()

    # Shift the moving averages by the desired number of periods
    df['short_ma'] = df['short_ma'].shift(periods=20)
    df['long_ma'] = df['long_ma'].shift(periods=40)

    # Fill in any missing values in the shifted moving averages using the values from the previous periods
    df['short_ma'] = df['short_ma'].bfill()
    df['long_ma'] = df['long_ma'].bfill()

    # Get the latest close price and moving averages
    close = df['close'].iloc[-1]
    short_ma = df['short_ma'].iloc[-1]
    long_ma = df['long_ma'].iloc[-1]

    # Check if we should buy
    if close > short_ma and position is None:
        # Get the available balance of Ether
        ether_balance = exchange.fetch_balance()['ETH']['free']

        # Place a market buy order for the entire balance
        exchange.create_market_buy_order(symbol, ether_balance)

        # Set the position variable to the amount of Ether purchased
        position = ether_balance

        # Set the holding start time
        holding
        # Check if we should sell
    elif close < long_ma and time.time - holding_start_time > holding_period * 24 * 60 * 60 and position is not None:
        # Place a market sell order for the entire position
        exchange.create_market_sell_order(symbol, position)

        # Set the position variable to None
        position = None
        
    # Sleep for one minute
    time.sleep(60)

import schedule
#loop bot forever
new_var = schedule.every(15).seconds.do(bot)
 

while True:
    try:
        print.run_pending
    except:
        print('Sleeping')
