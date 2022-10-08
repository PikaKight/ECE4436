from enum import auto
from socket import *
from base64 import *
import ssl



EMAIL = input("Email: ")
PASSWORD = input("Password: ") 
RCPT = input("Recipent: ")
SUBJECT_LINE = input("Subject: ")
MESSAGE = input("Msssage: ")

msg = f"{MESSAGE}. \r\nI love computer networks!" 
endmsg = "\r\n.\r\n"


# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailServer = 'smtp.gmail.com'
mailPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))

#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response. 
heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024).decode() 
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

#Account Autehtication
# Fill in start
strtlscmd = "STARTTLS\r\n".encode()
clientSocket.send(strtlscmd)
recv2 = clientSocket.recv(1024)

sslClientSocket = ssl.wrap_socket(clientSocket)

ENCODE_EMAIL = b64encode(EMAIL.encode())
ENCODE_PSW = b64encode(PASSWORD.encode())

authcmd = "AUTH LOGIN\r\n"
sslClientSocket.send(authcmd.encode())
recv3 = sslClientSocket.recv(1024)
print(recv3)

sslClientSocket.send(ENCODE_EMAIL + "\r\n".encode())
recv4 = sslClientSocket.recv(1024)
print(recv4)

sslClientSocket.send(ENCODE_PSW + "\r\n".encode())
recv5 = sslClientSocket.recv(1024)
print(recv5)
# Fill in end


# Send MAIL FROM command and print server response.
 
# Fill in start
mailFrom = f"Mail FROM: <{EMAIL}>\r\n."   
sslClientSocket.send(mailFrom.encode())
recv6 = sslClientSocket.recv(1024).decode()
print(recv6)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptto = f'RCPT TO: <{RCPT}>\r\n'
sslClientSocket.send(rcptto.encode())
recv7 = sslClientSocket.recv(1024)
print(recv7)
# Fill in end


# Send DATA command and print server response.

# Fill in start
data = 'DATA\r\n'
sslClientSocket.send(data.encode())
recv8 = sslClientSocket.recv(1024)
print(recv8)
# Fill in end


# Send message data.
# Fill in start
sslClientSocket.send(f"Subject: {SUBJECT_LINE}\n\n{MESSAGE}".encode())
# Fill in end


# Message ends with a single period.
# Fill in start
sslClientSocket.send(endmsg.encode())
recv9 = sslClientSocket.recv(1024)
print(recv9)
# Fill in end


# Send QUIT command and get server response.
# Fill in start
quitcmd = 'QUIT\r\n'
sslClientSocket.send(quitcmd.encode())
recv10 = sslClientSocket.recv(1024)
print(recv10)
# Fill in end