#!/usr/bin/python

from irc import *

HOST = "irc.freenode.net"
PORT = 6667
NICK = "Py_Bot_tester"
DEBUG = True
CHAN = "#PyBotTestChan"

irc = IRC() # constructor!
irc.connect(HOST, PORT, CHAN, NICK)

while True:
    data = irc.get_data()
    print data

    if "PRIVMSG" in data and CHAN in data and "!test" in data:
        irc.send_msg(CHAN, "You tested me!")
