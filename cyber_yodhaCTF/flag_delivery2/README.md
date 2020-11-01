### flag delivery 2

This challenge looks like file repair looking at the file in a hex editor I see the Magic numbers for PNG and the IHDR chunk are wrong. Fixing those:

PNG magic numbers
```
89 50 4E 47 0D 0A 1A 0A
```

updated hex
```
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0078 0000 0229 0806 0000 0069 29fc  ...x...).....i).
00000020: a900 0001 4169 4343 5049 4343 2050 726f  ....AiCCPICC Pro
00000030: 6669 6c65 0000 28cf 6360 6012 492c 28c8  file..(.c``.I,(.
00000040: 6161 6060 c8cd 2b29 0a72 7752 8888 8c52  aa``..+).rwR...R
00000050: 607f c2c0 c9c0 c2c0 c720 ca60 9a98 5c5c  `........ .`..\\
00000060: e018 10e0 0354 c200 a351 c1b7 6b0c 8c20  .....T...Q..k.. 
00000070: fab2 2ec8 2caf ce96 9487 fe4b 4ebc 3d5e  ....,......KN.=^
00000080: cce3 2a6a 3d81 013f e04a 492d 4e06 d27f  ..*j=..?.JI-N...
00000090: 8038 35b9 a0a8 8481 8131 05c8 562e 2f29  .85......1..V./)
```

file remains unable to open, hmm
trying in pngcheck I see

```
invalid chunk name "�DeT" (ffffffd9 44 65 54)
  chunk �DeT at offset 0x003cb, length 16384:  illegal reserved-bit-set chunk
```

my guess is to correct this chunk to the correct name, trying common PNG chunks I realise IDAT works

```
000003b0: 3c57 8851 0000 4000 4944 4154 7801 ed9d  <W.Q..@.IDATx...
```

no the png renders and we get the flag


![img](broken.png)

CYCTF{Br0k3n_1m@g3s_@r3_@_p@1n_1n_th3_b@ck}