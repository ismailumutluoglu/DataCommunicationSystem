def even_parity(data: bytes):
    ones = sum(bin(b).count("1") for b in data)
    return str(ones % 2)
