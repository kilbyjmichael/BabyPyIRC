import socket
import sys

class IRC:
    
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_msg(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " :" + msg + "\n")

    def connect(self, server, port, chan, nick):
        print "Connecting to... " + server
        self.irc.connect((server, port))
        self.irc.send('NICK ' + nick + '\n')
        self.irc.send('USER Py_Bot Py_Bot Py_Bot :Py+Bot IRC\n')
        self.irc.send('JOIN ' + chan + '\n')
        self.irc.send('PRIVMSG ' + chan + ' :Test Print.\n')
        return "Connected!"

    def ping_pong(data):
        if data.find('PING') != -1: #If PING is Found in the Data
            self.irc.send('PONG ' + data.split()[1] + '\n') #Send back a PONG

    def get_data(self):
        data = self.irc.recv(2040) # get me some data!

        if data.find('PING') != -1: #If PING is Found in the Data
            self.irc.send('PONG ' + data.split()[1] + '\n') #Send back a PONG

        return data
