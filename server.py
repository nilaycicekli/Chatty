# establishing connections.
import socket
# handling multiple connections.
import select

header_length = 10

ip_address = socket.gethostname()
port_number = 1234

# socket object.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #allows us to reconnect.
server_socket.bind((ip_address, port_number))


server_socket.listen()
print(f"listening...")

socket_list = [server_socket]

clients = {}


# server recieves messages from all client sockets
def receive_message(client_socket):
    try:
        message_header = client_socket.recv(header_length)

        if not len(message_header):
            return False

        message_length = int(message_header.decode("utf-8").strip())

        return {
            "header": message_header,
            "data": client_socket.recv(message_length)
        }

    except:
        return False


while True:
    read_sockets, _, exception_sockets, = select.select(socket_list, [], socket_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:

            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue

            socket_list.append(client_socket)

            clients[client_socket] = user

            print(f"accepted connection from {client_address[0]}:{client_address[1]},"
                  f"username: {user['data'].decode('utf-8')}")

        else:
            message = receive_message(notified_socket)

            if message is False:
                print(f"closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                socket_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]

            username = user['data'].decode('utf-8')

            print(f"received message from {username}:{message['data'].decode('utf-8')}")

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        socket_list.remove(notified_socket)
        del clients[notified_socket]