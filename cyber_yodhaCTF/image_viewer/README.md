### image viewer

get the image

`wget https://cyberyoddha.baycyber.net/files/2c6afadf4a0bd700c651e8d7c4040389/shoob_2.jpeg\?token\=eyJ1c2VyX2lkIjo3LCJ0ZWFtX2lkIjo0MjcsImZpbGVfaWQiOjV9.X5zO5Q.u-Xyvn3z4-AGTCUoWpOChWOPqg4 -O shoob.jpeg`

we are given the image here

![img](shoob.jpeg)

running exiftool we get the flag in the metadata

`exiftool shoob.jpeg`

```
ExifTool Version Number         : 12.08
File Name                       : shoob.jpeg
Directory                       : .
File Size                       : 11 kB
File Modification Date/Time     : 2020:09:08 20:47:13+01:00
File Access Date/Time           : 2020:10:31 02:44:45+00:00
File Inode Change Date/Time     : 2020:10:31 02:44:10+00:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
X Resolution                    : 1
Y Resolution                    : 1
Exif Byte Order                 : Big-endian (Motorola, MM)
Make                            : Shoob Phone
Camera Model Name               : Shoob 1
Resolution Unit                 : None
Software                        : MacOs ofc
Artist                          : Shoobs 4 life
Y Cb Cr Positioning             : Centered
Copyright                       : 2020
Exif Version                    : 0231
Date/Time Original              : 2020:09:04 17:09:04
Create Date                     : 2020:09:04 17:08:59
Components Configuration        : Y, Cb, Cr, -
User Comment                    : CORONA
Flashpix Version                : 0100
Owner Name                      : SHOOB
Lens Make                       : Canon 3
Lens Model                      : Shoob
Lens Serial Number              : CYCTF{h3h3h3_1m@g3_M3t@d@t@_v13w3r_ICU}
Image Width                     : 180
Image Height                    : 280
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 180x280
Megapixels                      : 0.050
```


flag: CYCTF{h3h3h3_1m@g3_M3t@d@t@_v13w3r_ICU}
