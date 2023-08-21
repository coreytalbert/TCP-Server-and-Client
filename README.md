# TCP-Server-and-Client
Basic multithreaded TCP server and client in Python.

This project implements a simple Python HTTP server for TCP connections. The server incudes basic security functionality to prevent access to certain files and directories. The server responds to HTTP requests by responding with a standard HTTP header and, if appropriate, the requested file. The project includes a few HTML files and a directory simulating a basic website for testing purposes.

This implementation takes advantage of Pythons threading library to enable the server to handle multiple requests simultaneously. When a connection is accepted, the server creates a new thread. The thread runs a function that contains the logic to parse the response and respond appropriately, and always closes the connection before the end of the thread’s lifetime. The implementation ensures that every request is handled before the server is shutdown by forcing the main thread to wait to join every running thread before exiting.
