### matryoshka doll

title implies it will be a series of nested files, time to wip out binwalk

`binwalk -Me dolls.jpg`

```
Scan Time:     2021-03-16 18:12:43
Target File:   /home/kali/Documents/rough/pico/2021/keygen/dolls.jpg
MD5 Checksum:  24b3a2ae66f966bc8193ab352c1dd12d
Signatures:    391

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378942, uncompressed size: 383937, name: base_images/2_c.jpg
651600        0x9F150         End of Zip archive, footer length: 22


Scan Time:     2021-03-16 18:12:44
Target File:   /home/kali/Documents/rough/pico/2021/keygen/_dolls.jpg.extracted/base_images/2_c.jpg
MD5 Checksum:  402d2b3641a33fca5001e0de49191ae0
Signatures:    391

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196042, uncompressed size: 201444, name: base_images/3_c.jpg
383804        0x5DB3C         End of Zip archive, footer length: 22
383915        0x5DBAB         End of Zip archive, footer length: 22


Scan Time:     2021-03-16 18:12:44
Target File:   /home/kali/Documents/rough/pico/2021/keygen/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/3_c.jpg
MD5 Checksum:  025573312971c1c2c49719e7c1c3180d
Signatures:    391

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 428 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
123606        0x1E2D6         Zip archive data, at least v2.0 to extract, compressed size: 77650, uncompressed size: 79806, name: base_images/4_c.jpg
201422        0x312CE         End of Zip archive, footer length: 22


Scan Time:     2021-03-16 18:12:44
Target File:   /home/kali/Documents/rough/pico/2021/keygen/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/4_c.jpg
MD5 Checksum:  fc1048511b32f506a3f19a7bd2c1afe4
Signatures:    391

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 320 x 768, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
79578         0x136DA         Zip archive data, at least v2.0 to extract, compressed size: 62, uncompressed size: 81, name: flag.txt
79784         0x137A8         End of Zip archive, footer length: 22

```

at the very deepest level we see flag.txt

reading we get picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}