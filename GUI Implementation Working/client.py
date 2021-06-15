import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('127.0.0.1', 55555))
        msg = tkinter.Tk()
        msg.withdraw()
        self.nickname = simpledialog.askstring("Nickname", "Enter Your Nickname ", parent=msg)
        if self.nickname == 'admin':
            msg2 = tkinter.Tk()
            msg2.withdraw()
            self.password = simpledialog.askstring("Password", "Enter Your password ", parent=msg2)
        self.gui_done = True
        self.running = True
        self.thread_stop = True
        gui_thread = threading.Thread(target=self.gui_loop)

        gui_thread.start()

    # print("---------------------------------Client is running----------------------------")
    # nickname = input("Enter\'s Your Nickname : ")
    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="lightgray")
        self.chat_label = tkinter.Label(self.win, text=self.nickname, bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)
        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)

        self.text_area.config(state='disabled')
        self.msg_label = tkinter.Label(self.win, text="Message", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)
        self.input_area = tkinter.Text(self.win, height=5)
        self.input_area.pack(padx=20, pady=5)
        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        self.gui_done = True

        self.win.protocol("WM_DELETE_WINDOW", self.stop)
        self.win.mainloop()

    def write(self):
        try:

            if self.thread_stop:
                #   break
                message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"  # get the whole text ie 1.0 to end
                if message[len(self.nickname) + 2:].startswith('$'):
                    if self.nickname == 'admin':
                        if message[len(self.nickname) + 2:].startswith('$kick'):
                            self.sock.send(f'KICK {message[len(self.nickname) + 2 + 6:]}'.encode('ascii'))
                            self.input_area.delete('1.0', 'end')
                        elif message[len(self.nickname) + 2:].startswith('$ban'):
                            self.sock.send(f'BAN {message[len(self.nickname) + 2 + 5:]}'.encode('ascii'))
                            self.input_area.delete('1.0', 'end')
                    else:
                        if self.gui_done:
                            self.text_area.config(state='normal')
                            self.text_area.insert('end', 'You have no powers to perform any commands!')
                            self.text_area.yview('end')
                            self.text_area.config(state='disabled')
                else:
                    self.sock.send(message.encode('ascii'))
                    self.input_area.delete('1.0', 'end')
            else:
                if self.gui_done:
                    self.text_area.config(state='normal')
                    self.text_area.insert('end',
                                          "Thread Cancelled out ! Can't write you are not longer connected to the "
                                          "server, try relaunching the "
                                          "client!")  # append message in text area at the end
                    self.text_area.yview('end')
                    self.text_area.config(state='disabled')
        except:
            if self.gui_done:
                self.text_area.config(state='normal')
                self.text_area.insert('end',
                                      "Can't write you are not longer connected to the server, try relaunching the "
                                      "client!")  # append message in text area at the end
                self.text_area.yview('end')
                self.text_area.config(state='disabled')

    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode('ascii')  # nick
                print(message)
                if message == 'NICK':
                    self.sock.send(self.nickname.encode('ascii'))  # nick
                    message2 = self.sock.recv(1024).decode('ascii')
                    print(message2)  # if ban #ban#pass
                    if message2 == 'pass':
                        self.sock.send(self.password.encode('ascii'))  # pass
                        if self.sock.recv(1024).decode('ascii') == 'Incorrect':
                            if self.gui_done:
                                self.text_area.config(state='normal')
                                self.text_area.insert('end',
                                                      "Your password is incorrect ,connection broke!")  # append message in text area at the end
                                self.text_area.yview('end')
                                self.text_area.config(state='disabled')
                                self.sock.close()
                                self.thread_stop = False
                                break
                    elif message2 == 'BAN':
                        print('You are banned , can\'t connect to server')
                        if self.gui_done:
                            self.text_area.config(state='normal')
                            self.text_area.insert('end',
                                                  'You are banned , can\'t connect to server')  # append message in text area at the end
                            self.text_area.yview('end')
                            self.text_area.config(state='disabled')
                            self.sock.close()
                            self.thread_stop = False
                            break
                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', message)  # append message in text area at the end
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                msage = "Server is closed or there is an error occured! \n Try Reconnecting"
                if self.gui_done:
                    self.text_area.config(state='normal')
                    self.text_area.insert('end', msage)  # append message in text area at the end
                    self.text_area.yview('end')
                    self.text_area.config(state='disabled')
                    self.thread_stop = False
                self.sock.close()
                break
            except:
                msage = "Server is closed or there is an error occured! \n Try Reconnecting"
                if self.gui_done:
                    self.text_area.config(state='normal')
                    self.text_area.insert('end', msage)  # append message in text area at the end
                    self.text_area.yview('end')
                    self.text_area.config(state='disabled')
                    self.thread_stop = False
                self.sock.close()
                break

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)


# if nickname == 'admin' :
# password = input('Enter the Password: ')
# client =
# client.connect(('127.0.0.1', 55555))

# thread_stop= False

client = Client()
