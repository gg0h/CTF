import binascii

for i in range(89):
    with open(f'..\\CTF_rough\\flag({i})') as fh:
        t = fh.read().strip()
        hex = t[8:-1]
        print(i, binascii.unhexlify(hex))