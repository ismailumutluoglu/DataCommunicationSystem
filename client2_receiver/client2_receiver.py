import socket
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from common import crc, parity, parity2d, hamming, checksum

HOST, PORT = "127.0.0.1", 6000

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Client 2 waiting...")
    conn, _ = s.accept()

    packet = conn.recv(2048).decode()
    data, method, sent_control = packet.split("|", 2)
    b = data.encode()

    computed = {
        "PARITY": parity.even_parity(b),
        "2D_PARITY": parity2d.parity_2d(b),
        "CRC16": crc.crc16_ccitt(b),
        "HAMMING": hamming.hamming_encode(b),
        "CHECKSUM": checksum.internet_checksum(b)
    }[method]

    print("Received Data :", data)
    print("Method :", method)
    print("Sent Check Bits :", sent_control)
    print("Computed Check Bits :", computed)
    print("Status :", "DATA CORRECT" if sent_control == computed else "DATA CORRUPTED")
