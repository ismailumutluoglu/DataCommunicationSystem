import socket
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from common import crc, parity, parity2d, hamming, checksum

HOST, PORT = "127.0.0.1", 5000

print("""
1 - Even Parity
2 - 2D Parity
3 - CRC16
4 - Hamming Code
5 - Internet Checksum
""")

choice = input("Choose method: ")
data = input("Enter text: ")
b = data.encode()

methods = {
    "1": ("PARITY", parity.even_parity(b)),
    "2": ("2D_PARITY", parity2d.parity_2d(b)),
    "3": ("CRC16", crc.crc16_ccitt(b)),
    "4": ("HAMMING", hamming.hamming_encode(b)),
    "5": ("CHECKSUM", checksum.internet_checksum(b))
}

method, control = methods[choice]
packet = f"{data}|{method}|{control}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(packet.encode())

print("Sent Packet:", packet)
