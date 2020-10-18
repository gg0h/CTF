from pwn import *

r = remote("env2.hacktober.io", 5001)

number_per_iter = 1
current = 666

stairway = []

for i in range(30):
    s = []
    for j in range(number_per_iter):
        s.append(str(current))
        current += 1
    stairway.append(" ".join(s))
    number_per_iter += 1

print(r.recvuntil("deal."))

# print("\\n".join([i for i in stairway]))
r.sendline("".join([i for i in stairway]))

print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())