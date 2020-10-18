### red rum

"We want you to infiltrate DEADFACE as a programmer. Thing is, they're picky about who they bring in. They want to make sure you're the real deal when it comes to programming. Generate a list of numbers 1-500. For each number divisible by 3, replace it with Red; for each number divisible by 5, replace it with Rum. For numbers divisible by both 3 AND 5, replace it with RedRum."

FooBar, basic programming challenge, completed with this script

```python
s = ""

red_rum = []

for i in range(1, 501):
    if (i % 3 == 0) and (i % 5 == 0):
        s = "RedRum"
    elif i % 3 == 0:
        s = "Red"
    elif i % 5 == 0:
        s = "Rum"
    else:
        s = str(i)
    red_rum.append(s)

print(",".join(red_rum))
```

and then piped to netcat

python3 ape.py | cat - | nc env2.hacktober.io 5000

flag{h33eeeres_j0hnny!!!}