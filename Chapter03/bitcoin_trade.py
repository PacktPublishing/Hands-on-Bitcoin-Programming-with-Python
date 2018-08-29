#!/usr/bin/python

# import modules
# Make sure to copy the exchanges from https://github.com/dursk/bitcoin-price-api
# to the same location as this ascript
from exchanges.bitfinex import Bitfinex
import smtplib

# Function to send email
def trigger_email(msg):
    # Change these to your email details
    email_user = "abcd@gmail.com" 
    email_password = "password"
    smtp_server = 'gmail smtm server'
    smtp_port = 587
    email_from = "abcd@gmail.com"
    email_to = "abcd@gmail.com"

    # login to the email server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_user, email_password)

    # send email
    server.sendmail(email_from, email_to, msg)
    server.quit()

# define buy and sell threshholds for Bitcoin
buy_thresh = 6500
sell_thresh = 6500

# get Bitcoin prices
btc_sell_price = Bitfinex().get_current_bid()
btc_buy_price = Bitfinex().get_current_ask()

# Trigger Buy email if buy price is lower then threadhold
if btc_buy_price < buy_thresh:

    email_msg = """
    Bitcoin Buy Price is %s which is lower then
    threshhold price of %s.
    Good time to buy!""" % (btc_buy_price, buy_thresh)

    trigger_email(email_msg)

# Trigger sell email if sell price is higher then threashold
if btc_sell_price > sell_thresh:

    email_msg = """
    Bitcoin sell Price is %s which is higher then
    threshhold price of %s.
    Good time to sell!""" % (btc_sell_price, sell_thresh)

    trigger_email(email_msg)
