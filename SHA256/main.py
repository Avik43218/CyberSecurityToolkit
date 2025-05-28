import struct
import bitwise_functions as bit
from constants import Constants as C

def padding(message: bytes):

    message_len_bits = len(message) * 8
    message += b'\x80'  # Add 1 bit at the end
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    
    message += struct.pack('>Q', message_len_bits)

    return message

def sha256(message: bytes):

    message = padding(message=message)
    hashes = C.H.copy()

    for chunk_start in range(0, len(message), 64):
        chunk = message[chunk_start: chunk_start + 64]
        w = list(struct.unpack('>16L', chunk)) + [0] * 48
        
        for i in range(16, 64):
            w[i] = bit.σ1(w[i - 2]) + w[i - 7] + bit.σ0(w[i - 15]) + w[i - 16]

        a, b, c, d, e, f, g, h = hashes

        for i in range(64):
            T1 = h + bit.Σ1(e) + bit.ch(e, f, g) + C.K[i] + w[i]
            T2 = bit.Σ0(a) + bit.maj(a, b, c)
            h = g
            g = f
            f = e
            e = d + T1
            d = c
            c = b
            b = a
            a = T1 + T2

    hashes = [(x + y) & 0xFFFFFFFF for x, y in zip(hashes, [a, b, c, d, e, f, g, h])]

    return ''.join(f'{x:08x}' for x in hashes)
