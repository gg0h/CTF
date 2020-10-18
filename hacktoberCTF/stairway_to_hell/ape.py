from pwn import *

r = remote("env2.hacktober.io", 5001)

number_per_iter = 1
current = 666

stairway = []

for i in range(30):
    for j in range(number_per_iter):
        stairway.append(current)
        current += 1
    number_per_iter += 1

# print(" ".join([str(i) for i in stairway]))

print(r.recvuntil("deal."))

r.sendline(" ".join([str(i) for i in stairway]))

print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())