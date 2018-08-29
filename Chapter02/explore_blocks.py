#!/usr/bin/env python

# import blockchain library
from blockchain import blockexplorer

# get a particular block
block = blockexplorer.get_block('0000000000000000002e90b284607359f3415647626447643b9b880ee00e41fa')

print("Block Fee: %s\n" % block.fee)
print("Block size: %s\n" % block.size)
print("Block transactions: %s\n" % block.transactions)

# get the latest block
block = blockexplorer.get_latest_block()
