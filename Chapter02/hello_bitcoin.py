#!/usr/bin/env python
'''
Title - Hello Bitcoin

This program demonstrates the creation of
- private key,
- public key
- and a bitcoin address.
'''
# import bitcoin
from bitcoin import *

# Generate Private key
my_private_key = random_key()
print("Private Key: %s\n" % my_private_key)

# Generate Public Key
my_public_key = privtopub(my_private_key)
print("Public Key: %s\n" % my_public_key)

# Create a bitcoin address
my_bitcoin_address = pubtoaddr(my_public_key)
print("Bitcoin Address: %s\n" % my_bitcoin_address)
