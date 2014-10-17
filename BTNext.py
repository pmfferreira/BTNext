b = bytearray(open('_b.ini', 'rb').read())
for i in range(len(b)):
    b[i] = ~b[i] & 0xFF
    b[i] = ((b[i] & 0x0F) << 4) | ((b[i] & 0xF0) >> 4)
open('b_text.txt', 'wb').write(b)

b = bytearray(open('_t.ini', 'rb').read())
for i in range(len(b)):
    b[i] = ~b[i] & 0xFF
    b[i] = ((b[i] & 0x0F) << 4) | ((b[i] & 0xF0) >> 4)
open('t_text.txt', 'wb').write(b)
