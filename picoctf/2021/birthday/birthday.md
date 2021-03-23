### It is my birthday

"I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. Anyway, see if you're invited by submitting 2 PDFs to my website. http://mercury.picoctf.net:63578/"

so we need two slighty different files that are pdfs that have the same md5sum

I found two identical files [here](https://www.mscs.dal.ca/~selinger/md5collision/)

and simply renamed their prefix, as this is the extent of the "is a pdf" checking

