### password3 

this is just a case of recersing all the steps, base64 and the XOR, done with this script

```
import base64

base64_string = "FgwWARMuF2UhPQotZScKFTsxCjcVJmYKY2FqCiE9FSEmCjJlMTksKA=="
base64_bytes = base64_string.encode("ascii")
pass_bytes = base64.b64decode(base64_bytes)
finalPass = pass_bytes.decode("ascii")

print(finalPass)

newPass = []

for i in range(0,40):
    newPass.append(chr(ord(finalPass[i]) ^ 0x55))

print("".join(newPass))
```

alternatively done in [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)XOR(%7B'option':'Hex','string':'0x55'%7D,'Standard',false)&input=Rmd3V0FSTXVGMlVoUFFvdFpTY0tGVHN4Q2pjVkptWUtZMkZxQ2lFOUZTRW1DakpsTVRrc0tBPT0)

CYCTF{B0th_x0r_@nd_b@s3_64?_th@ts_g0dly}