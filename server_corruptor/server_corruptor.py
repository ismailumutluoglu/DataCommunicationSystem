import socket
import random

HOST = "127.0.0.1"
PORT_IN = 5000
PORT_OUT = 6000

def corrupt(data):
    if len(data) == 0:
        return data
    i = random.randint(0, len(data)-1)
    return data[:i] + chr(random.randint(65, 90)) + data[i+1:]

with socket.socket() as s:
    s.bind((HOST, PORT_IN))
    s.listen()
    print("Server waiting...")
    conn, _ = s.accept()

    packet = conn.recv(2048).decode()
    data, method, control = packet.split("|", 2)

    corrupted_data = corrupt(data)
    new_packet = f"{corrupted_data}|{method}|{control}"

    with socket.socket() as out:
        out.connect((HOST, PORT_OUT))
        out.sendall(new_packet.encode())

    print("Forwarded:", new_packet)
