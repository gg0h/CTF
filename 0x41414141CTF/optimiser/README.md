### Optimiser

remote: nc 207.180.200.166 9660

we are greeted with,

'you will be given a number of problems give me the least number of moves to solve them'
'level 1: tower of hanoi'

the minimum number of moves for a tower of hanoi problem can be found with (2 ^ k) -1

where k is the length of the first tower

so to solve we can find the length of the tower, calculate the min number of moves and send back

I implemented this via pwntools

```py
from pwn import *

p = remote('207.180.200.166', 9660)

print(p.recvuntil("hanoi", timeout=1))

for _ in range(25):
    tower = p.recvuntil(']').decode()
    print(tower)
    if tower:
        l = len(tower.split(','))
        payload = str(2 ** l -1)
        print(payload)
        p.sendline(payload)
        continue
    break
```

'level 2 : merge sort, give me the count of inversions'

I was confused at first but with some googling I realised this is just the number of times a number must swap places to be sorted via merge sort.
This can be found by counting the number of elements smaller than the current element, summed for each element in the list, like so

```py
def get_inv_count(arr, n): 
  
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count
```

with this I have solved both parts, and receive the flag with this script

```py
from pwn import *

p = remote('207.180.200.166', 9660)

print(p.recvuntil("hanoi", timeout=1))

for _ in range(25):
    tower = p.recvuntil(']').decode()
    print(tower)
    if tower:
        l = len(tower.split(','))
        payload = str(2 ** l -1)
        print(payload)
        p.sendline(payload)
        continue
    break

def get_inv_count(arr, n): 
  
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count

print(p.recvuntil("inversions", timeout=1))

for _ in range(25):
    line = p.recvuntil(']').decode()
    i = line.index('[')
    print(f'i = {i}')
    j = line.index(']')
    print(f'j = {j}')
    line = line[i:j+1] # trim out the preceeding '>'
    arr = eval(line)
    print(arr)
    inv_count = get_inv_count(arr, len(arr))
    print(inv_count)
    p.sendline(str(inv_count))

p.interactive()
```

flag{g077a_0pt1m1ze_3m_@ll}
