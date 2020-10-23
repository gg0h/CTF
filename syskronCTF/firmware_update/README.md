### Firmware Update

```
The crypto software LibrePLC at BB Industry is continuously receiving updates. Unfortunately, the responsible employee left the company a few weeks ago and hasn't deployed the most recent firmware with important security updates. He just left a note with 5157CA3SDGF463249FBF.

We urgently need the new firmware!
```

I'll be honest I don't understand how this challenge was worth 500, it was way to easy

we are given a zip, `"LibrePLC_firmware_pack.zip"`

unzipping we get get three files

```
LibrePLC_fw_1.0.0.zip
LibrePLC_fw_1.0.1.zip
LibrePLC_fw_1.0.2.zip
```

all are password protected

the first can be unzipped using the note from the description as a password

giving two files

```
key
LibrePLC_fw_1.0.0.bin
```

after reading key, I discovered it's a python function taking one file as an argument
so I tried the binary and got `7SYSCC3076BDCTF13CC9CTFA6CB7SYSCC3076CD56579549EC5AB533EN03AFC1F9N`
I tried this as a password for LibrePLC_fw_1.0.1.zip and it worked!
I repeated the same for LibrePLC_fw_1.0.1.bin and got another string `CSYS0BBA60E46ABB19C5BC0CSYS0CCK60EQ1NC41E2C5DDA4C5C7D45E096162`
which worked as the password for LibrePLC_fw_1.0.2.zip

finally I ran strings on the binary LibrePLC_fw_1.0.2.bin and found the flag (not sure if this part is intended)

syskronCTF{s3Cur3_uPd4T3}