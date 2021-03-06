import socket
import sys
import wikipedia

class IRC:
    
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_msg(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " :" + msg + "\n")
        
    def join_chan(self, chan):
        self.irc.send('JOIN ' + chan + "\n")
        # add to chan list, so bot funcitons on all chans

    def connect(self, server, port, chan, nick):
        print "Connecting to... " + server
        self.irc.connect((server, port))
        self.irc.send('NICK ' + nick + '\n')
        self.irc.send('USER Py_Bot Py_Bot Py_Bot :Py+Bot IRC\n')
        self.irc.send('JOIN ' + chan + '\n')
        
        self.irc.send('JOIN ' + "#PyBotDebugChan" + '\n')
        self.irc.send('PRIVMSG ' + "#PyBotDebugChan" + ' :Test Print.\n')
        return "Connected!"

    def get_data(self):
        data = self.irc.recv(2040) # get me some data!
        
        if "PING" in data: #If PING is Found in the Data
            self.irc.send("PONG " + data.split(':')[1] + '\n') #Send back a PONG
            
        return data

    def test_data(self, data, chan):
        if "PRIVMSG" in data and chan in data and "!test" in data:
            user = data.split('!')[0].replace(':', '')
            self.send_msg(chan, user + " tested me!")
        elif "PRIVMSG" in data and chan in data and "!wikipedia" in data:
            command = ':'.join(data.split (':')[2:])
            com_args = ''.join(command.replace('!wikipedia ', ''))
            user = data.split('!')[0].replace(':', '')
            try: wiki_return = str(wikipedia.summary(com_args))
            except UnicodeEncodeError:
                error = "Cant unicode"
                return self.send_msg(chan, error)
            final_send = user + " your wikipedia search: " + wiki_return
            self.send_msg(chan, final_send)
        elif "PRIVMSG" in data and chan in data and "!join" in data:
            command = ':'.join(data.split (':')[2:])
            com_args = ''.join(command.replace('!join ', ''))
            self.join_chan(com_args)
        elif "sageinventor" in data and "!quit" in data:
            # self.irc.send("QUIT :leaving bro\n") dosn't work
            self.cleanup()
        elif "PRIVMSG" in data and chan in data and "!say" in data:
            command = ':'.join(data.split (':')[2:])
            com_args = ''.join(command.replace('!say ', ''))
            # no works: say_chan = ''.join(com_args.split(''))
            # self.send_msg("#PyBotDebugChan", say_chan)
            self.send_msg(chan, com_args)

    def cleanup(self):
        self.irc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.irc.shutdown(socket.SHUT_RDWR)
        
    #def leave!
