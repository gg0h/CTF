### Security Headers

`"Can you please check the security-relevant HTTP response headers on www.senork.de. Do they reflect current best practices?"`

this one was quite simple, navigate to the site and by opening devtools and inspecting the response headers, you will see

```
content-encoding: gzip
content-security-policy: default-src 'none'; img-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self'; font-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'; manifest-src 'self'
content-type: text/html; charset=UTF-8
date: Wed, 21 Oct 2020 12:39:47 GMT
etag: W/"5f7567d5-1774"
feature-policy: fullscreen 'self'
flag-policy: syskronCTF{y0u-f0und-a-header-flag}
last-modified: Thu, 01 Oct 2020 05:23:33 GMT
referrer-policy: no-referrer
server: nginx
status: 304
strict-transport-security: max-age=31536000; includeSubdomains; preload
vary: Accept-Encoding
x-content-type-options: nosniff
x-frame-options: DENY
x-xss-protection: 1; mode=block
```

__syskronCTF{y0u-f0und-a-header-flag}__