#!/usr/bin/env python3
import socket

serverPort = 6789

# SOCK_STREAM means TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Avoid TIME_WAIT socket lock [DO NOT REMOVE]
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Open port and start listening
serverSocket.bind(("", serverPort))
serverSocket.listen(0)
print(serverSocket)

print("The server is ready to receive")
try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        print(connectionSocket)
        connectionSocket.send(("PORT " + str(serverPort)).encode())
        sentence = connectionSocket.recv(1024).decode()
        print(sentence)
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
        connectionSocket.close()
except KeyboardInterrupt:
    serverSocket.close()
