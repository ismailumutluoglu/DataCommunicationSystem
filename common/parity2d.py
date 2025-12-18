def parity_2d(data: bytes):
    matrix = [bin(b)[2:].zfill(8) for b in data]

    row_parity = [str(row.count("1") % 2) for row in matrix]

    col_parity = []
    for i in range(8):
        col_parity.append(
            str(sum(int(row[i]) for row in matrix) % 2)
        )

    return "".join(row_parity) + "|" + "".join(col_parity)
