#Network with Python
#transport layer ---- programs comunacating across 2 computers 
#tcp = trnasport controll protocol /// sockets (like a tele line )

#ports live on secure ports 

import socket
mysocket = socket(socket.af_INET,socket.SOCK_STREAM)
mysocket.connect(("data.pr4e.org",80))
