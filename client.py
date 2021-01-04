import socket
import select
import errno
import sys

# tell server username
# send and receive messages


header_length = 10

ip_address = socket.gethostname()
port_number = 1234

client_username = input("username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_address,port_number))
client_socket.setblocking(False)

username = client_username.encode('utf-8')
username_header = f"{len(username):<{header_length}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    message = input(f"{client_username} > ")

    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message) :< {header_length}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        while True:
            message_header = client_socket.recv(header_length)
            if not len(username_header):
                print("connection closed by server")
                sys.exit()

            username_length = int(username_header.decode('utf-8').strip())

            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(header_length)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            # Print message
            print(f'{username} > {message}')

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()
        continue

    except Exception as e:
        print('Reading error: '.format(str(e)))
        sys.exit()