### data store

we are given the web page 

`https://cyberyoddha.baycyber.net:33002/`

Upon visiting the webpage we are prompted with a username and password login.
Based on the challenge name I guessed this would be SQL injection

so I tried:

```
username: admin'--
password: plzwork
```

The injection succeeded and I got the flag

```
Here is your flag
CYCTF{1_l0v3_$q1i}
```

flag: CYCTF{1_l0v3_$q1i}