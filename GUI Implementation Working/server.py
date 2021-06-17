import socket
import threading

host = '127.0.0.1'
port = 55555

# to start server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast_msg(message, bmsg):
    for client in clients:
        client.send(message)
    print("\n----------------- Broadcast Log ------------")
    print("\t\t\t\t\t" + bmsg)
    print("------------")


def manage(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message.startswith('KICK'):
                if nicknames[clients.index(client)] == 'admin':
                    name_to_kick = message[5:].strip('\n')

                    kick_user(name_to_kick)
                else:
                    client.send('Command was refused!'.encode('ascii'))
            elif message.startswith('BAN'):
                if nicknames[clients.index(client)] == 'admin':
                    name_to_ban = message[4:].strip('\n')
                    kick_user(name_to_ban)
                    with open('bans.txt', 'a') as f:
                        f.write(f'{name_to_ban}\n')
                    print(f'{name_to_ban} was banned from the server')
                else:
                    client.send('Command was refused!'.encode('ascii'))
            else:
                message2 = message.encode('ascii')
                broadcast_msg(message2, message)
        except:  # on exception
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                bmsg = f'{nickname} has left the chat.'
                broadcast_msg(
                    bmsg.encode('ascii'), bmsg)
                print("Client has left the chat with nickname ", nickname)
                nicknames.remove(nickname)
                break


def receive():
    while True:
        client, address = server.accept()
        print(f'New Client is connected with the Address = {str(address)}')
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')  # nick
        with open('bans.txt', 'r') as f:
            bans = f.readlines()
        if f'{nickname}\n' in bans:
            client.send('BAN'.encode('ascii'))  # ban
            client.close()
            continue
        if nickname == 'admin':
            client.send('pass'.encode('ascii'))
            password = client.recv(1024).decode('ascii')  # pass
            if password != 'adminpass':
                client.send('Incorrect'.encode('ascii'))
                client.close()
                continue
        nicknames.append(nickname)
        clients.append(client)
        print(f'Client\'s nickname : {nickname}')
        bmsg = f'{nickname} has just joined the chat !\n'
        broadcast_msg(bmsg.encode('ascii'), bmsg)
        client.send(f'Successfully Connected to Server\n '.encode('ascii'))
        thread = threading.Thread(target=manage, args=(client,))
        thread.start()


def kick_user(name):
    try:
        if name in nicknames:
            name_index = nicknames.index(name)
            client_to_kick = clients[name_index]
            clients.remove(client_to_kick)
            client_to_kick.send('You were kicked  '.encode('ascii'))
            client_to_kick.close()
            nicknames.remove(name)
            bmsg = f'{name} was kicked by an admin'
            broadcast_msg(bmsg.encode('ascii'), bmsg)
    except:
        print("error here")


print("-----------------------------server is running-------------------------")
receive()
