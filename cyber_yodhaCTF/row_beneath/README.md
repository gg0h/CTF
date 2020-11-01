### Row Beneath

get image 

`wget https://cyberyoddha.baycyber.net/files/1fc688c615def9c4ee27d09a3dc79029/plan.png\?token\=eyJ1c2VyX2lkIjo3LCJ0ZWFtX2lkIjo0MjcsImZpbGVfaWQiOjYwfQ.X5zP-A.SC_vHxr8ZHBR3VkYblqCzyCNK44 -O plan.png`

![plan](plan.jpeg)

run exiftool, says it is a JPEG?

```
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
```

found nothing with steghide

`steghide extract -sf plan.jpeg`

try binwalk

`binwalk plan.jpeg `

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
```
nothing
 
 after wasting more time in stegsolve, we get the flag in strings 

 CYCTF{L00k_1n_th3_h3x_13h54d56}