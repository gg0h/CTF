### Screenshot

looking at the image I immediately notice a flag directory at `C:\Program Files\flag`

running in stegsolve I noticed:

- red plane 1 - doesn't seem so significant to me
- green plane 0 - This seems more interesting...

![green 0](green_0.bmp)
![red 1](red_1.bmp)

morse code sequence found, but appears to make no sense

after wasting some time trying to decode the morse code I spent more time trying to extract data from green 0 and I found that using the "extract data" function
in stegsolve I can get some data from green plane 0. After trying enough variants I found the correct settings that in the text output gave the flag. 

![extract options](extract.png)

000000007379736b 726f6e4354467b73  ....sysk ronCTF{s
33637233545f6d33 73533467337d0000  3cr3T_m3 sS4g3}..

syskronCTF{s3cr3T_m3sS4g3}

