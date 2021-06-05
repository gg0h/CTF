# Phase Stream 1

## Description

The aliens are trying to build a secure cipher to encrypt all our games called "PhaseStream". They've heard that stream ciphers are pretty good. The aliens have learned of the XOR operation which is used to encrypt a plaintext with a key. They believe that XOR using a repeated 5-byte key is enough to build a strong stream cipher. Such silly aliens! Here's a flag they encrypted this way earlier. Can you decrypt it (hint: what's the flag format?) 

2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904

This challenge will raise 33 euros for a good cause.

## Solution

since we know the first five bytes of the flag as "CHTB{"

we can xor this with the cipher to get the key, and then xor with the key to get the full flag.

done with this python script

```py
from pwn import xor

c_string = "2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904"
cipher = bytes.fromhex(c_string)

known = b"CHTB{"

print(f"[*] known: {known}")
print(f"[*] cipher: {cipher}")
print("[*] xoring known with cipher...")

x_res = xor(cipher, known)

print(x_res)

key = x_res[:5]

print(f"[*] Key found: {key}")

print(xor(cipher, key))
```