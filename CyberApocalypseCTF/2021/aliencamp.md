# Alien Camp

## Description

The Ministry of Galactic Defense now accepts human applicants for their specialised warrior unit, in exchange for their debt to be erased. We do not want to subject our people to this training and to be used as pawns in their little games. We need you to answer 500 of their questions to pass their test and take them down from the inside.
This challenge will raise 33 euros for a good cause.

## Solution

upon interacting via netcat, we are prompted with

```
1. ❓
2. Take test!
> 
```

pressing one provides a key like so

```
🌞 -> 5 🍨 -> 9 ❌ -> 55 🍪 -> 17 🔥 -> 24 ⛔ -> 26 🍧 -> 62 👺 -> 8 👾 -> 3 🦄 -> 83
```

pressing two begins a series of 500 questions

```
Question 1:                 
🌞 * ❌ * 🔥 * 🦄                                                                                                                  
                     
Answer:                                                  

```

I wrote a script to interact with this via pwntools.

I first parse the key it gives to form a dictionary, and then read the question, substitute the emojis for their numbers and eval the string with some boilerplate I found online

my script is here, pls excuse the messiness :)

```py
from pwn import *
import ast
import operator as op

# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}


def parse_q():
    print(r.recvline_startswith("Question").decode())
    print(r.recvline().decode())
    q = r.recvline()[:-4].strip()
    print(r.recv().decode())
    print(q.decode())
    subd = substitute_str(q).decode()
    print(subd)
    result = eval_expr(subd)
    print(result)
    r.sendline(str(result))
    #print(r.recv().decode())

def substitute_str(q):
    return b" ".join([i  if i not in pairs.keys() else pairs[i] for i in q.split(b" ")])

def eval_expr(expr):
    """
    >>> eval_expr('2^6')
    4
    >>> eval_expr('2**6')
    64
    >>> eval_expr('1 + 2*3**(4^5) / (6 + -7)')
    -5.0
    """
    return eval_(ast.parse(expr, mode='eval').body)

def eval_(node):
    if isinstance(node, ast.Num): # <number>
        return node.n
    elif isinstance(node, ast.BinOp): # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)


if __name__ == "__main__":
    r = connect("138.68.189.41", 31663)

    print(r.recv(1024).decode())
    r.sendline("1")
    print(r.recvlines(2))
    key = r.recvline()
    print(key.decode())
    split = key.split(b" ")
    pairs = {split[i]: split[i+2] for i in range(0, len(split[:-1]), 3)}
    print(pairs)

    print(r.recv().decode())

    r.sendline("2")
    for i in range(500):
        parse_q()

    print(r.recv().decode())
```
CHTB{3v3n_4l13n5_u53_3m0j15_t0_c0mmun1c4t3}