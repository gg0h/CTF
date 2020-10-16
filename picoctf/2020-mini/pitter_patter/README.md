### Pitter Patter Platter

After the second hint was dropped telling us to look into slack space I found 
figured out this command, using a tool from TSK (The Sleuth Kit)

```
blkls -i raw -s suspicious.dd.sda1
```

which printed out `} 1 9 3 7 b e f c _ 3 < _ | L m _ 1 1 1 t 5 _ 3 b { F T C o c i` not sure why the p is missing

reversing this gives the flag

`picoCTF{b3_5t111_mL|_<3_cfeb7391}`