import socket
import time
import os
import struct
import telnet

def connect(ip, port):
    return socket.create_connection((ip, port))

def toBi(x):
    return struct.pack('<I', x)
#if you want to handle 64bit, change 'I' to ''Q

def toUnBi(x):
    return struct.unpack('<I', x)[0]

def interacts(s):
    print('________ interactive mode ________')
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()

s = connect('127.0.0.1', 4000)

#write code here

interact(s)
