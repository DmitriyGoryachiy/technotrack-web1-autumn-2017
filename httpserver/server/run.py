# -*- coding: utf-8 -*-
import socket
import os

def get_response(request):
    return 'Hello mister! You are '+request



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', 8000))  # define whom we will listen and on which port
server_socket.listen(1) # maximum  amount of sockects we are going to listen


print ('Started')




while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print(client_socket)
        print ('Got new client', client_socket.getsockname())  #
        request_string = client_socket.recv(2048)  #set up max size of accepted data from client
        urequest_string = request_string.decode("utf-8")
        print(urequest_string)
        client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        '''#preUrl = urequest_string.split('http://localhost:8000/')
        #print(preUrl)
        #leftUrl = preUrl[1].split('\r\n')
        if leftUrl[0] == 'files/test1.txt':
            client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
            f = open("/home/garfin/TechnoTreck/WebServices/technotrack-web1-autumn-2017/httpserver/files/test1.txt")
            str = ''+f.read()
            client_socket.send(str.encode())
            client_socket.close()
        elif leftUrl[0] == 'files/test2.txt':
            client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
            f = open("/home/garfin/TechnoTreck/WebServices/technotrack-web1-autumn-2017/httpserver/files/test2.txt")
            str = ''+f.read()
            client_socket.send(str.encode())
            client_socket.close() 
        elif leftUrl[0] == 'files/': 
            files = os.listdir('/home/garfin/TechnoTreck/WebServices/technotrack-web1-autumn-2017/httpserver/')
            client_socket.send(('\n'.join(files)).encode())
            client_socket.close()
        elif leftUrl[0] == 'test/':
            client_socket.send(request_string)
            client_socket.close()
        elif leftUrl[0] == '':
            
        '''
        preUserAgent = urequest_string.split('User-Agent')
        userAgent=preUserAgent[1].split('\r\n')
        client_socket.send(get_response(userAgent[0]).encode())  # sending response to user
        client_socket.close()
        '''
        
        '''
    except KeyboardInterrupt:  # catching exception if user decided to close conection
        print ('Stopped')
        server_socket.close()  # stoping the server
        exit()
