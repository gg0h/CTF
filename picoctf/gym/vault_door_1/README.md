### vault door 1

a little more complex this time 

the password can be easily found in

```java
public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e';
    }
```

I reformatted this to

```text
0  == 'd'
10 == '_'
11 == 't'
12 == 'H'
1  == '3'
13 == '3'
14 == '_'
15 == 'c'
16 == 'H'
17 == '4'
18 == 'r'
19 == '4'
20 == 'c'
21 == 'T'
22 == '3'
23 == 'r'
24 == '5'
2  == '5'
25 == '_'
26 == '7'
27 == '5'
28 == '0'
29 == '9'
30 == '2'
31 == 'e'
3  == 'c'
4  == 'r'
5  == '4'
6  == 'm'
7  == 'b'
8  == 'l'
9  == '3'
```

and got the string with this command

```bash
sort a.txt -n | cut -f 3 -d ' ' | tr -d "\n'"
```

1. numeric sort
2. grab the third field
3. remove newlines and single quotes


picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}