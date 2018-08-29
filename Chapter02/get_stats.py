#!/usr/bin/env python

# import blockchain library
from blockchain import statistics

# get the stats object
stats = statistics.get()

# get and print Bitcoin trade volumne
print("Bitcoin Trade Volume: %s\n" % stats.trade_volume_btc)

# get and print Bitcoin mined
print("Bitcoin mined: %s\n" % stats.btc_mined)

# get and print Bitcoin market price in usd
print("Bitcoin market price: %s\n" % stats.market_price_usd)
