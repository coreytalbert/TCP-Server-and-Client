from socket import *
from time import strftime, gmtime
import sys  # In order to terminate the program
from threading import Thread, enumerate, main_thread

def shutdown(serverSocket):
    threads = enumerate()
    print(threads)
    for i in range(0, len(threads)):
        if (threads[i] != main_thread()): 
            threads[i].join()
    serverSocket.close()
    sys.exit()

def handle(connectionSocket, request):
    print(Thread.ident)

    header = ["",
              "Date: " + strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime()) + "\r\n",
              "Server: " + sys.platform + "\r\n",
              "\r\n"]
    outputdata = ""

    filename = request.split()[1].strip("/")
    if (filename.startswith("grades")):
        outputdata = "<h1>403 Forbidden</h1>Access denied."
        header[0] = "HTTP/1.1 403 Forbidden\r\n"
    else:
        try:
            with open(filename) as f:
                outputdata = f.read()
                header[0] = "HTTP/1.1 200 OK\r\n"
                print("Serving " + filename + " to " +
                      str(connectionSocket.getsockname()))
        except IOError:
            outputdata = "<h1>404 Not Found</h1>File not found."
            header[0] = "HTTP/1.1 404 Not Found\r\n"

    response = ''.join(header)
    if (outputdata):
        response += outputdata
    response += "\r\n"

    connectionSocket.send(response.encode())
    connectionSocket.close()

def main():
    serverPort = 6789
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(0)

    try:
        while True:
            print("Ready to serve...")
            connectionSocket, addr = serverSocket.accept()
            request = connectionSocket.recv(1024).decode()
            Thread(target=handle, args=[connectionSocket, request]).start()
    except KeyboardInterrupt:
        shutdown(serverSocket)
        
    shutdown(serverSocket)

if __name__ == "__main__":
    main()
