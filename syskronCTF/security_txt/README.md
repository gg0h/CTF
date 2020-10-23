### Security.txt

After some time wasting looking into the stale email address I had a look at the PGP key


```
-----BEGIN PGP PUBLIC KEY BLOCK-----

mDMEX1IeNRYJKwYBBAHaRw8BAQdAGkGzrffXJoSEuPxIZ+ADdMAH1COdISkwrmFC
ZyCWGP+0X0JCIEluZHVzdHJ5IGEucy4gUFNJUlQgKHN5c2tyb25DVEZ7V2gwLXB1
dDMtZmxhZzMtMW50by0wcGVuUEdQLWtleTM/Pz99KSA8cHNpcnRAYmItaW5kdXN0
cnkuY3o+iJYEExYIAD4WIQQb0Dqaer1Y3W4NxowpcUAVAB/owgUCX1IeNQIbAwUJ
AE8aAAULCQgHAgYVCgkICwIEFgIDAQIeAQIXgAAKCRApcUAVAB/owkYsAP9uMtdg
0YInW+JgxdZbGhP7dQS7Bv1fKARx2GDcVUt7BAD/cgkM1BSC3jT1PuutPA7HDwC7
709QGbka8o/G1t9EBwE=
=mLiy
-----END PGP PUBLIC KEY BLOCK-----
```

running `gpg --list-packets encryption_key.asc`

we get the output

```
# off=0 ctb=98 tag=6 hlen=2 plen=51
:public key packet:
        version 4, algo 22, created 1599217205, expires 0
        pkey[0]: [80 bits] ed25519 (1.3.6.1.4.1.11591.15.1)
        pkey[1]: [263 bits]
        keyid: 29714015001FE8C2
# off=53 ctb=b4 tag=13 hlen=2 plen=95
:user ID packet: "BB Industry a.s. PSIRT (syskronCTF\x7bWh0-put3-flag3-1nto-0penPGP-key3???\x7d) <psirt@bb-industry.cz>"
# off=150 ctb=88 tag=2 hlen=2 plen=150
:signature packet: algo 22, keyid 29714015001FE8C2
        version 4, created 1599217205, md5len 0, sigclass 0x13
        digest algo 8, begin of digest 46 2c
        hashed subpkt 33 len 21 (issuer fpr v4 1BD03A9A7ABD58DD6E0DC68C29714015001FE8C2)
        hashed subpkt 2 len 4 (sig created 2020-09-04)
        hashed subpkt 27 len 1 (key flags: 03)
        hashed subpkt 9 len 4 (key expires after 60d0h0m)
        hashed subpkt 11 len 4 (pref-sym-algos: 9 8 7 2)
        hashed subpkt 21 len 5 (pref-hash-algos: 10 9 8 11 2)
        hashed subpkt 22 len 3 (pref-zip-algos: 2 3 1)
        hashed subpkt 30 len 1 (features: 01)
        hashed subpkt 23 len 1 (keyserver preferences: 80)
        subpkt 16 len 8 (issuer key ID 29714015001FE8C2)
        data: [255 bits]
        data: [255 bits]
```

with the flag

`"BB Industry a.s. PSIRT (syskronCTF\x7bWh0-put3-flag3-1nto-0penPGP-key3???\x7d) <psirt@bb-industry.cz>"`

syskronCTF{Wh0-put3-flag3-1nto-0penPGP-key3???}