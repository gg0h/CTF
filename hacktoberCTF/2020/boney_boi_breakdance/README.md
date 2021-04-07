### Boney Boi Breakdance

passphrase protected file

after running strings, interesting results

- n20EhXZCce
- maineH

none useful, after reverse searching the image I tried cracking it with strings from the [wikipedia page](https://en.wikipedia.org/wiki/Danse_Macabre) using stegcracker

`python3 -m stegcracker dance_to_death.jpg wordlist.txt`

that gave me the flag 

flag{d4n53_m4c4br3_nuremberg}
