#!/usr/bin/python

from irc import *
# MAKE A DEBUG CHAN TO SEND DEBUG DATA TO!

HOST = "irc.freenode.net"
PORT = 6667
NICK = "Py_Bot_tester"
DEBUG = True
CHAN = "#PyBotTestChan"

irc = IRC() # constructor!
irc.connect(HOST, PORT, CHAN, NICK)

try:
    while True:
        data = irc.get_data()
        irc.test_data(data, CHAN)
        print data
except KeyboardInterrupt:
    irc.cleanup()
