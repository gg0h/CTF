### Mind your P's and Q's

given

c: 964354128913912393938480857590969826308054462950561875638492039363373779803642185
n: 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e: 65537

simple RSA problem, let's put n into factordb

p = 2434792384523484381583634042478415057961
q = 650809615742055581459820253356987396346063

now we can solve with 

```py
import binascii

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinverse(a, m): # modular inverse
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

c = 964354128913912393938480857590969826308054462950561875638492039363373779803642185
n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e = 65537

p = 2434792384523484381583634042478415057961
q = 650809615742055581459820253356987396346063

phi = ( q - 1 ) * ( p - 1 )
d = modinverse( e, phi )
print(d)
print('======')
m = pow( c, d, n )
print(m)
print('======')


print(repr(binascii.unhexlify(hex(m)[2:])))
```

