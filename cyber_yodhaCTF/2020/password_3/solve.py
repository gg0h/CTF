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