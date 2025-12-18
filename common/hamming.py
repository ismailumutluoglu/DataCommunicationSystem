def hamming_encode(data: bytes):
    encoded = []
    for b in data:
        bits = bin(b)[2:].zfill(8)
        for i in range(0, 8, 4):
            d = list(map(int, bits[i:i+4]))
            p1 = d[0] ^ d[1] ^ d[3]
            p2 = d[0] ^ d[2] ^ d[3]
            p3 = d[1] ^ d[2] ^ d[3]
            encoded.append(f"{p1}{p2}{d[0]}{p3}{d[1]}{d[2]}{d[3]}")
    return "|".join(encoded)
