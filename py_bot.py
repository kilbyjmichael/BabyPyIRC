#!/usr/bin/python

'''Py_Bot! Testing'''

import socket

HOST = "irc.freenode.net"
PORT = 6667
NICK = "Py_Bot_tester"
DEBUG = True
CHAN = ""
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def check_debug(debug):
    if debug == True:
        chan = "#PyBotTestChan"
    elif debug == False:
        chan = "#michael"
    return chan

def connect_to_irc(host,port,nick,chan,debug):
    chan = check_debug(debug)
    
    irc.connect((host,port))

    irc.send('NICK ' + nick + '\r\n')
    irc.send('USER Py_Bot Py_Bot Py_Bot :Py+Bot IRC\r\n')
    irc.send('JOIN ' + chan + '\r\n')
    irc.send('PRIVMSG ' + chan + ' :Test Print.\r\n')
    return "connected"

def ping_pong(data):
    if data.find('PING') != -1: #If PING is Found in the Data
        irc.send('PONG ' + data.split()[1] + '\r\n') #Send back a PONG

def message_send(msg, chan):
    irc.send('PRIVMSG ' + chan + ' :' + msg + '\r\n')

def test_commands(data, chan): # broken
    irc.send('PRIVMSG ' + chan + ' :Test working.\r\n')
    # :sageinventor!~sageZNC@104.131.97.211 PRIVMSG #PyBotTestChan :Hello
    if data.find('PRIVMSG') != -1: #if PRVMSG is found, start
        irc.send('PRIVMSG ' + chan + ' :' + "you said something" + '\r\n')

def main():
    try:
        print connect_to_irc(HOST,PORT,NICK,CHAN,DEBUG)
        while True:
            data = irc.recv(4096)# Make Data the Receive Buffer
            print data #Print the Data to the console(For debug purposes)
            message_send("test print again", CHAN)
            #ping_pong(data)
            #test_commands(data, CHAN)
    finally:
        # cleanup!
        irc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        irc.shutdown(socket.SHUT_RDWR)
        

if __name__ == "__main__": main()
        
