import socket
import threading
import sqlite3 as sq
import os
# саздание сокета
HOST = "127.0.0.1"
PORT = 65432
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()


name = []
cl = []

def new_client(conn,addr,cone):
    while 1:
        # палучение данниь о клиенте
        data  = conn.recv(1024).decode('UTF-8')
        data = data.split(' ')

        
        
        # праверка в базе данниь и отправка резултат к клиенты
        with cone:
            cur = cone.cursor()
            zapros = "SELECT user FROM client WHERE user == '"+data[1]+"' and parol == '"+data[2]+"'"
            zapros2 = "SELECT user FROM client WHERE user == '"+data[1]+"'"
            cur.execute(zapros2)
            id = cur.fetchall()
            
        if id != []:
            id=id[0][0]   
            if data[0] == 'l':
                cur.execute(zapros)
                id = cur.fetchall()
                if id != []:
                    id=id[0][0] 
                    conn.sendall(("ok"+str(id)).encode())
                    print("connected",data[1],data[2])
                 
                    break
                else:
                    conn.sendall("no".encode())
                    print("sxal name, parol")
            else:
                conn.sendall("ok".encode())
        else:
            if data[0] == 'l':
                conn.sendall("no".encode())
                print("sxal name, parol")
            else:
                with cone:
                    cur = cone.cursor()
                    cur.execute("INSERT INTO client VALUES(?,?)",(data[1], data[2]))
                    cur.execute(zapros)
                    id = cur.fetchall()[0][0]
                    cone.commit()
                conn.sendall(("no"+str(id)).encode())
                print("new acaunt",data[1],data[2])
                
                break
            
        if data == [""]: break

def poisk(conn,cone,data):
    with cone:
        cur = cone.cursor()
        zapros = "SELECT * FROM client WHERE user LIKE '%"+data+"%' LIMIT 10"
        cur.execute(zapros)
        id = cur.fetchall()
        if id != []: 
            text = [i[0] for i in id]
            conn.sendall(("pook "+" ".join(text)).encode())
            print("poisk",text)
        else: 
            conn.sendall(("pono").encode())

def send(data):
    contact = data.split()[0]
    if contact in name:
        send_ms = data[len(contact)+1:]
        i = name.index(contact)
        cl[i].sendall(("se"+send_ms).encode())
        print(send_ms)
        print(contact,data[len(contact):])

def getdata(conn,cone):
    while 1:
        try:
            data = conn.recv(1024).decode('UTF-8')
            if data[:2] == 'po':
                poisk(conn,cone,data[2:])
            elif data[:2] == 'se':
                send(data[2:])
        except:
            break

def con():
   
    conn, addr = s.accept()                 # падключени клиента
    threading.Thread(target=con).start()    # новии паток
    
    # падклыучение к базе данни
    path = os.path.dirname(os.path.abspath(__file__))
    cone = sq.connect(path+"\\DB.sqlite")
    
    

    # палучение id клиента
    id = conn.recv(1024).decode('UTF-8')
    # print(id)
    if id == "-": new_client(conn,addr,cone)        #если клиент не имеет id
    else:
        name.append(id)
        cl.append(conn)
        print(id)
        getdata(conn,cone)

    try:
        i = cl.index(conn)
        cl.remove(conn)
        name.pop(i)
    except:
        pass

    cone.close()
    conn.close()
        



# падклыучение сокетов
tr1 = threading.Thread(target=con)
tr1.start()
# while 1:
#     print(name)