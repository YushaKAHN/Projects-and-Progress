import socket
mysocket = socket.socket(socket.AF_INET, socket.socket_STREAM)
mysocket.connect(("data.pr4e.org,80"))
cmd = "GET https//data.pr4e.pr4e.orge/romeo.text HTTP/1.0\n\n".encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
    mysocket.close()
