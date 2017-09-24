# -*- coding: utf-8 -*-
import socket
import os

def get_response(request):
    return "Hello mister! " \
           "You are "+request



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', 8000))  # define whom we will listen and on which port
server_socket.listen(2) # maximum  amount of sockects we are going to listen


print ('Started')

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        #print(client_socket)
        print ('Got new client', client_socket.getsockname())  #
        request_string = client_socket.recv(2048)  #set up max size of accepted data from client
        urequest_string = request_string.decode("utf-8")
        preGet = urequest_string.split()
        isGet = preGet[0]
        #print("f"+isGet+"f")
        #print(urequest_string)
        #client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        if isGet == "GET":
            preUrl = urequest_string.split('GET ')
            leftUrl = preUrl[1].split(' HTTP')
            #print('q'+leftUrl[0]+'q')
            tail =  ''+leftUrl[0]

            if leftUrl[0] == '/media/test1.txt':
                #print('flag')
                f = open("../files/test1.txt")
                str = ''+f.read()
                client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
                client_socket.send(str.encode())
                client_socket.close()
            elif leftUrl[0] == '/media/test2.txt':
                f = open('../files/test2.txt')
                str = ''+f.read()
                client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
                client_socket.send(str.encode())
                client_socket.close()
            elif leftUrl[0] == '/media/':
                files = os.listdir('../')
                client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
                client_socket.send('\n\r'.join(files).encode())
                client_socket.close()
            elif leftUrl[0] == '/test/':
                client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
                client_socket.send(request_string)
                client_socket.close()
            elif leftUrl[0] == '/':
                preUserAgent = urequest_string.split('User-Agent')
                userAgent=preUserAgent[1].split('\r\n')
                client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
                client_socket.send(get_response(userAgent[0]).encode())  # sending response to user
                client_socket.close()
            else:
                client_socket.send(b"HTTP/1.1 404 Not found\r\nContent-Type: text/html\r\n\r\n")
                client_socket.send("Page not found".encode())
                client_socket.close()
        else:
            client_socket.send(b"HTTP/1.1 405 Not found\r\nContent-Type: text/html\r\n\r\n")
            client_socket.send("Not alloud method".encode())
            client_socket.close()
    except KeyboardInterrupt:  # catching exception if user decided to close conection
        print ('Stopped')
        server_socket.close()  # stoping the server
        exit()
