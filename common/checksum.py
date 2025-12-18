def internet_checksum(data: bytes):
    if len(data) % 2 == 1:
        data += b'\x00'

    total = 0
    for i in range(0, len(data), 2):
        total += (data[i] << 8) + data[i+1]
        total = (total & 0xFFFF) + (total >> 16)

    return format(~total & 0xFFFF, "04X")
