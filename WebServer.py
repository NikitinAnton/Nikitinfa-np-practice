import socket
import os

WORKING_DIR = os.getcwd()  # Возвращает название папки/директории, где находится скрипт

server = socket.socket()
server.bind(('localhost', 80))  # 127.0.0.1

server.listen(1)

while True:

    conn, addr = server.accept()
    print(addr)
    request = conn.recv(10240).decode().split('\n')

    method, url, protocol = request[0].split(' ')
    url = os.path.join(WORKING_DIR, url[1:])

    print(url)
    code = "404 Not Found"
    body = ""


    if os.path.isfile(url):
        code = "200 OK"
        body = open(url, 'r').read()

    response = f"HTTP/1.1 {code}\n"
    response += "Server: my_dummy_server"
    response += "\n\n"
    response += body
    conn.send(response.encode())
    conn.close()
    print("Connection closed\n")
