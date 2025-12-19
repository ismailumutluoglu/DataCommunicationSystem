# 🔌 Socket Error Detection Simulator

**Data Communication System - Error Detection Simulation Project**

This project was developed as part of the **Data Communication System** course to simulate various **error detection algorithms** used in data communication. The project performs data transmission between three components using socket programming and demonstrates how errors that may occur during transmission are detected.

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Architecture](#-architecture)
- [Supported Algorithms](#-supported-algorithms)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)

---

## 🎯 About the Project

This simulation is designed to practically understand the error detection mechanisms learned in the **Data Communication System** course. The detection of errors that may occur in data sent over noisy channels in data communication is simulated as follows:

1. **Sender (Client 1)** → Encodes data with the selected error detection method and sends it
2. **Server (Corruptor)** → Receives the data, randomly corrupts it, and forwards it
3. **Receiver (Client 2)** → Receives the data, computes check bits, and detects whether there are errors

---

## 🏗 Architecture

```
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│   CLIENT 1      │         │     SERVER      │         │   CLIENT 2      │
│   (Sender)      │ ──────► │   (Corruptor)   │ ──────► │   (Receiver)    │
│   Port: 5000    │         │   In:5000       │         │   Port: 6000    │
│                 │         │   Out:6000      │         │                 │
│ • Data input    │         │ • Random        │         │ • Error check   │
│ • Algorithm     │         │   character     │         │ • Result        │
│   selection     │         │   modification  │         │   display       │
│ • Check bit     │         │                 │         │                 │
│   calculation   │         │                 │         │                 │
└─────────────────┘         └─────────────────┘         └─────────────────┘
```

---

## 🔬 Supported Algorithms

| #   | Algorithm             | Description                                                                                      |
| --- | --------------------- | ------------------------------------------------------------------------------------------------ |
| 1   | **Even Parity**       | Simple single-bit parity check. Makes the count of 1s in data bits even.                         |
| 2   | **2D Parity**         | Two-dimensional parity. Computes parity for both rows and columns, providing stronger detection. |
| 3   | **CRC-16 CCITT**      | Cyclic Redundancy Check. A powerful error detection algorithm based on polynomial division.      |
| 4   | **Hamming Code**      | An algorithm capable of both error detection and single-bit error correction.                    |
| 5   | **Internet Checksum** | 16-bit checksum algorithm used in TCP/IP protocols.                                              |

---

## ⚙ Installation

### Requirements

- Python 3.6+

### Steps

```bash
# Clone the repository
git clone https://github.com/username/SocketErrorDetection.git
cd SocketErrorDetection
```

> 📝 **Note:** No external libraries are required. Only Python standard library is used.

---

## 🚀 Usage

Open three separate terminal windows and run in order:

### 1. Start the Receiver (Terminal 1)

```bash
python client2_receiver/client2_receiver.py
```

> Output: `Client 2 waiting...`

### 2. Start the Server (Terminal 2)

```bash
python server_corruptor/server_corruptor.py
```

> Output: `Server waiting...`

### 3. Run the Sender (Terminal 3)

```bash
python client1_sender/client1_sender.py
```

### Example Run

**Sender (Client 1):**

```
1 - Even Parity
2 - 2D Parity
3 - CRC16
4 - Hamming Code
5 - Internet Checksum

Choose method: 3
Enter text: Hello
Sent Packet: Hello|CRC16|9D13
```

**Server:**

```
Server waiting...
Forwarded: HXllo|CRC16|9D13
```

**Receiver (Client 2):**

```
Client 2 waiting...
Received Data      : HXllo
Method             : CRC16
Sent Check Bits    : 9D13
Computed Check Bits: 45A2
Status             : DATA CORRUPTED
```

---

## 📁 Project Structure

```
SocketErrorDetection/
│
├── client1_sender/
│   └── client1_sender.py      # Data sender client
│
├── client2_receiver/
│   └── client2_receiver.py    # Data receiver client
│
├── server_corruptor/
│   └── server_corruptor.py    # Data corruptor server
│
├── common/                    # Common modules
│   ├── __init__.py
│   ├── parity.py              # Even Parity algorithm
│   ├── parity2d.py            # 2D Parity algorithm
│   ├── crc.py                 # CRC-16 CCITT algorithm
│   ├── hamming.py             # Hamming Code algorithm
│   └── checksum.py            # Internet Checksum algorithm
│
└── README.md
```

---

## 📚 Algorithm Details

### Even Parity

```python
# A parity bit is added so that the count of 1s in all bits is even
ones = sum(bin(b).count("1") for b in data)
parity_bit = ones % 2
```

### CRC-16 CCITT

```python
# Polynomial: 0x1021
# Initial value: 0xFFFF
# A 16-bit check value is produced using XOR and shift operations
```

### Internet Checksum

```python
# 16-bit words are summed
# Overflows are added (one's complement)
# The result is inverted
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/newFeature`)
3. Commit your changes (`git commit -m 'Added new feature'`)
4. Push to the branch (`git push origin feature/newFeature`)
5. Open a Pull Request

---

## 📄 License

This project was developed for educational purposes.

---

## 👨‍💻 Developer

Developed as part of the **Data Communication System** course project.

### 📖 Course Topics

The following course topics were practically implemented in this project:

- Error Detection & Error Correction
- Parity Check (Even/Odd Parity)
- Two-Dimensional Parity
- Cyclic Redundancy Check (CRC)
- Hamming Code
- Internet Checksum
- Socket Programming & Data Transmission

---

<p align="center">
  <i>⭐ Don't forget to star this project if you found it helpful!</i>
</p>
