import socket
import threading

print("---------------------------------Client is running----------------------------")
nickname = input("Enter\'s Your Nickname : ")

if nickname == 'admin' :
    password = input('Enter the Password: ')
client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

thread_stop= False
def receive():
    while True:
        global thread_stop
        if thread_stop:
            break
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
                message2=client.recv(1024).decode('ascii')
                if message2 == 'pass':
                    client.send(password.encode('ascii'))
                    if client.recv(1024).decode('ascii') == 'Incorrect':
                        print("Your password is incorrect ,connection broke!")
                        thread_stop= True
                elif message2=='BAN':
                    print('You are banned , can\'t connect to server')
                    client.close()
                    thread_stop=True
            else:
                print(message)
        except:

            print("Server is closed or there is an error occured!")
            client.close()
            break


def write():
    try:
        while True:
                if thread_stop:
                    break
                message = f'{nickname}: {input("")}'
                if message[len(nickname)+2:].startswith('$'):
                    if nickname == 'admin' :
                        if message[len(nickname)+2:].startswith('$kick'):
                            client.send(f'KICK {message[len(nickname) +2 + 6:]}'.encode('ascii'))
                        elif message[len(nickname)+2:].startswith('$ban'):
                            client.send(f'BAN {message[len(nickname) +2 + 5:]}'.encode('ascii'))
                    else:
                        print('You have no powers to perform any commands!')
                else:
                    client.send(message.encode('ascii'))
    except:
        print("Can't write you are not longer connected to the server, try relaunching the client!")
rcv_thread = threading.Thread(target=receive)
rcv_thread.start()
send_thread = threading.Thread(target=write)
send_thread.start()
