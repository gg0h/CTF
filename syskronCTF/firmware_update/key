#!/usr/bin python3
import hashlib #line:3
import sys #line:4
def check ():
        if len (sys .argv )==1 :#
                print ("No key for you")#
                sys .exit (0 )#line:9
        else :#line:10
                OOO0OOOOOO00000OO =sys .argv [1 ]#
                return OOO0OOOOOO00000OO #line:12
def get_it (OOO0OOOOO00000OOO ):#line:14
        with open (OOO0OOOOO00000OOO ,"rb")as O0000O000O00O0000 :#line:15
                O0O0O0OOO000OOO0O =O0000O000O00O0000 .read ()
                OO0O000O0OO000O0O =hashlib .sha256 (O0O0O0OOO000OOO0O ).hexdigest ()
        return OO0O000O0OO000O0O #line:18
def keys (OOOOOOOO00OOOOOOO ):#line:20
        O0OO00OOO00OOOOOO =OOOOOOOO00OOOOOOO [::-1 ][:10 ]#line:21
        O00O00O0O0O0O0000 =OOOOOOOO00OOOOOOO [5 :20 ][::-1 ]#line:22
        O00O00O0O0O0O0000 =O0OO00OOO00OOOOOO .replace ("1","0")[::-1 ].replace ("9","sys")#
        O0OO00OOO00OOOOOO =O00O00O0O0O0O0000 .replace ("a","k").replace ("4","q").replace ("b","c").replace ("5","kron")#line:24
        O0O000OO0000O000O =OOOOOOOO00OOOOOOO [23 :50 ][::-1 ].replace ("8","n")
        O0OO0OO0OOOOO0OO0 =OOOOOOOO00OOOOOOO [50 :61 ][::-1 ].replace ("7","ctf")#
        O0OO00O00000O00O0 =(O00O00O0O0O0O0000 +O0OO0OO0OOOOO0OO0 +O0OO00OOO00OOOOOO +O0O000OO0000O000O ).upper ()#
        return O0OO00O00000O00O0 #line:30
print (keys (get_it (check ())))
