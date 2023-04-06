def flippingBits(n):
    bi = bin(n)[2:]
    length_bi = len(bi)
    bi_32 = '0' * (32-length_bi)
    bi_32 = (bi_32 + bi)
    new_num = ''
    for d in bi_32:
        if d == '0':
            new_num += '1'
        else:
            new_num += '0'

    return int(new_num, 2)