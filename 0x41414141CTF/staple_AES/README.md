### staple AES

`nc 161.97.176.150 3167`

source:

```py
import os

import socketserver

import string

import threading

from time import *

import random

import time

import binascii



from Crypto.Cipher import AES

from Crypto.Util.Padding import pad



iv = b''

key = b''

flag = open("flag.txt", "rb").read().strip()



class Service(socketserver.BaseRequestHandler):



    def handle(self):

        assert len(flag) % 16 == 1

        blocks = self.shuffle(flag)

        ct = self.encrypt(blocks)

        self.send(binascii.hexlify(ct))



    def byte_xor(self, ba1, ba2):

        return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])



    def encrypt(self, blocks):

        curr = iv

        ct = []

        cipher = AES.new(key, AES.MODE_ECB)

        for block in blocks:

            curr = cipher.encrypt(curr)

            ct.append(self.byte_xor(block, curr))

        return b''.join(ct)



    def shuffle(self, pt):

        pt = pad(pt, 16)

        pt = [pt[i: i + 16] for i in range(0, len(pt), 16)]

        random.shuffle(pt)

        return pt



    def send(self, string, newline=True):

        if type(string) is str:

            string = string.encode("utf-8")



        if newline:

            string = string + b"\n"

        self.request.sendall(string)



    def receive(self, prompt="> "):

        self.send(prompt, newline=False)

        return self.request.recv(4096).strip()





class ThreadedService(

    socketserver.ThreadingMixIn,

    socketserver.TCPServer,

    socketserver.DatagramRequestHandler,

):

    pass





def main():



    port = 3167

    host = "0.0.0.0"



    service = Service

    server = ThreadedService((host, port), service)

    server.allow_reuse_address = True



    server_thread = threading.Thread(target=server.serve_forever)



    server_thread.daemon = True

    server_thread.start()



    print("Server started on " + str(server.server_address) + "!")



    # Now let the main thread just wait...

    while True:

        sleep(10)





if __name__ == "__main__":

    main()
```

because of this line
`assert len(flag) % 16 == 1`
we know that one of the blocks must be the closing brace and the rest padding, it's fair to assume we have three blocks of 16 bytes
```py
[b'flag{AAAAAAAAAAA', b'AAAAAAAAAAAAAAAA', b'}\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f']

known = b'}\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'
```

We know that the first block is always XOR'd with the same key, (the iv encrypted once) and because of the shuffle function we can connect many times to get a position such that each of the three blocks is in the first postion once. We can then XOR the knwon string to get potential values for the `curr` XOR variable, and XOR that with our first block fragements to decrypt

```py
s1 = "1210374ff7b52c4b265c3e4050e61d5445deb95cf4f78c13bcb4135d4365e32763305d63ac7c5657ec3ad64a021548e5"
s2 = "072e4b1f8fdb161b690c427c3c9b212f4b83ab64f8dfe67b94db150948638f647853330bd83a066f8b05ac22656e18dd"
s3 = "1c4d2577fb9d46230e3338145be071175ebdd73480b1dc2bdb8b6935241eb31f760e2133d4126c07a36aaa766e68749e"

a = binascii.unhexlify(s1[:32])
b = binascii.unhexlify(s2[:32])
c = binascii.unhexlify(s3[:32])

known = b'}\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'
def xor(x, y):
    return bytes([_a ^ _b for _a, _b in zip(x, y)])

aK = xor(known, a)
print(aK)
bK = xor(known, b)
print(bK)
cK = xor(known, c)
print(cK)
print("============")
print(xor(aK, b))
print(xor(aK, c))
print("============")

print(xor(bK, a))
print(xor(bK, c))
print("============")

print(xor(cK, a))
print(xor(cK, b))
```

```sh
b'o\x1f8@\xf8\xba#D)S1O_\xe9\x12['
b'z!D\x10\x80\xd4\x19\x14f\x03Ms3\x94. '
b'aB*x\xf4\x92I,\x01<7\x1bT\xef~\x18'
============
b'h1s_wa5_@_s3cr3t'
b"sR\x1d7\x03'eg'`\t[\x04\tcL"
============
b'h1s_wa5_@_s3cr3t'
b'flag{I_7h0ught_7'
============
b"sR\x1d7\x03'eg'`\t[\x04\tcL"
b'flag{I_7h0ught_7'

```



flag{I_7h0ught_7h1s_wa5_@_s3cr3t}