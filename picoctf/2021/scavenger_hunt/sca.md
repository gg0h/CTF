### Scavenger Hunt

http://mercury.picoctf.net:5080/

let's check robots

```
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

ah seems I skipped a bit

check source

`<!-- Here's the first part of the flag: picoCTF{t -->`

okay let's check js and css

in js a clue for robots.txt

in css

`/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */`

so now we got 

picoCTF{th4ts_4_l0t_0f_pl4c

seems 1 more

in .htaccess we find

```
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

ahh 1 more

I looked up hidden mac files [here](https://bytebitebit.com/macos-hidden-files-and-directories/)

trying .DS_store

`Congrats! You completed the scavenger hunt. Part 5: _35844447}`

picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_35844447}
