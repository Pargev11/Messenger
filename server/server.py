import socket
import threading
import sqlite3 as sq
import os
from sqlite3 import Error
import time

# саздание сокета
HOST = "127.0.0.1"
PORT = 65432
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

class server:
    def __init__(self,s):
        self.s = s
        self.connected_clients = {}

        threading.Thread(target=self.get_request).start()

    # палучение данни
    def get_request(self):

        conn, _ = self.s.accept()                 # падключени клиента

        # падклыучение к базе данни
        path = os.path.dirname(os.path.abspath(__file__))
        self.cone = sq.connect(path+"\\DB.sqlite")

        threading.Thread(target=self.get_request).start()

        # палучение имя клиента
        try:
            name = conn.recv(1024).decode('UTF-8')
            if name == "-": self.new_contact(conn)
        except:
            pass
        self.connected_clients[name] = conn
        with self.cone:
            cur = self.cone.cursor()
            zapros = F"SELECT sender,message,time FROM messages WHERE recipient == '{name}'"
            cur.execute(zapros)
            sqlist = cur.fetchall()
            if sqlist != []:
                # sqlist = sqlist)
                print(sqlist)
                res = []
                for i in range(len(sqlist)):
                    sqlist[i] = list(sqlist[i])
                    sqlist[i][2] = str(sqlist[i][2])
                    res = res+sqlist[i]
                    
                print(res)
                conn.sendall((" ".join(res)).encode())
                cur.execute(F"DELETE FROM messages  WHERE recipient == '{name}'")
                self.cone.commit()
            else:
                conn.sendall((" ").encode())

        while 1:
            try:
                print(self.connected_clients)
                data = conn.recv(1024).decode('UTF-8')
                if data == "": 
                    self.connected_clients.pop(name)
                    print(self.connected_clients)
                    break
                print(name,data)
                code, msg = data[:2], data[2:] 
                
                if code == "po":
                    self.search(msg,conn)
                elif code == "se":
                    self.send(msg,name,conn)
            except:
                self.connected_clients.pop(name)
                print(self.connected_clients)
                break

    def new_contact(self,conn):
        while 1:
            try:
                msg = conn.recv(1024).decode('UTF-8')
                
                code, msg = msg[:2], msg[2:] 
                
                # если нажал на loիn
                with self.cone:
                    cur = self.cone.cursor()
                    msg = msg.split()
                    name,password = msg[0], msg[1]
                    if code == 'lg':  
                        
                        zapros = "SELECT name FROM users WHERE name == '"+name+"' and password == '"+password+"'"
                        cur.execute(zapros)
                        names = cur.fetchall()
                        if names !=[]: 
                            conn.sendall(("ok").encode())
                            print('login', name, password)
                            break
                        else:
                            conn.sendall(("no").encode())
                    elif code == 'rg':
                        zapros = "SELECT name FROM users WHERE name == '"+name+"'"
                        cur.execute(zapros)
                        names = cur.fetchall()
                        if names ==[]: 
                            conn.sendall(("ok").encode())
                            print('signup', name, password)
                            cur.execute("INSERT INTO users VALUES(?,?)",(name, password))
                            self.cone.commit()
                            break
                        else:
                            conn.sendall(("no").encode())
                    else: break
            except:
                break
    def search(self,data,conn):
        
        with self.cone:
            cur = self.cone.cursor()
            zapros = "SELECT * FROM users WHERE name LIKE '%"+data+"%' LIMIT 10"
            cur.execute(zapros)
            names = cur.fetchall()
            if names != []: 
                
                text = [i[0] for i in names]
                conn.sendall(("po"+" ".join(text)).encode())
                print("poisk",text)
            else:
                conn.sendall("po".encode())

    def send(self,data,From,conn):
        data = data.split()
        To, msg  = data[0], data[1]
        print(From,To,msg)
        
        if To in self.connected_clients:
            self.connected_clients[To].sendall(("se"+From+" "+msg).encode())
        else:
            with self.cone:
                print(111,From,To,msg)
                cur = self.cone.cursor()
                cur.execute(F"INSERT INTO messages VALUES('{From}','{To}','{msg}','{time.time()}')")
                self.cone.commit()

        
s = server(s)


