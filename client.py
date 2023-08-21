#!/usr/bin/env python3
from socket import *

serverName = "127.0.0.1"
serverPort = 6789 

clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName,serverPort)) 
print(clientSocket.recv(1024).decode())

request = """GET /HelloWorld.html HTTP/1.1\r\n
    Host: www-net.cs.umass.edu\r\n
    User-Agent: Firefox/3.6.10\r\n
    Accept: text/html,application/xhtml+xml\r\n
    Accept-Language: en-us,en;q=0.5\r\n
    Accept-Encoding: gzip,deflate\r\n
    Accept-Charset: ISO-8859-1,utf-8;q=0.7\r\n
    Keep-Alive: 115\r\n
    Connection: keep-alive\r\n
    \r\n"""
clientSocket.send(request.encode()) 

response = clientSocket.recv(1024).decode()
print ("From Server:\n", response) 

clientSocket.close()