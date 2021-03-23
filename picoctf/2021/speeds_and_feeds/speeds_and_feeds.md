### speeds and feeds

There is something on my shop network running at mercury.picoctf.net:28067, but I can't tell what it is. Can you?

connecting and getting the instruction into a file `nc mercury.picoctf.net 28067`

the are some esoteric language on first inspection

the hint says to look for CNC machine language, I find out quickly it is G code

I found an online interpreter to run it [here](https://nraynaud.github.io/webgcode/)

picoCTF{num3r1cal_c0ntr0l_84d2d117}