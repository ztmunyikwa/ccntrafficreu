import os
import subprocess


#ssh into each client connect a route to all five of the server
#ssh into each server connect a route to all five of the clients 
#the servers send ccntraffic and the clients send ccndelphi

servers = ['h1x1', 'h1x2', 'h1x3', 'h1x4', 'h1x5']
clients = ['h4x2', 'h4x3', 'h4x4', 'h4x5', 'h4x6']

serverips = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5']
clientips = ['192.168.4.2', '192.168.4.3', '192.168.4.4', '192.168.4.5', '192.168.4.6']

for x in range(0, 5):
        os.system('ssh ' + "$"+ servers[x])
        os.system('cd /usr/local/bin')
        for y in range(0,5):
                os.system('./ccndc add ccnx:/ccnx.org tcp ' + clientips[y])
                print 'Connected '+ servers[x] + ' to '+ clients[y]
        os.system('exit');
