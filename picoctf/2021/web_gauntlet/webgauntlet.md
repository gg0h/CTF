### Web Gauntlet

we have to sqli the command 

`SELECT username, password FROM users WHERE username='<user_here>' AND password='<password_here>'`

the following strings are filtered by WAF 

`Filters: or and true false union like = > < ; -- /* */ admin`

we can bypass the admin filter using the `||` concatenation operator like so

`ad'||'min`

Now the problem is we can't just comment out the rest of the query because `--` and `/* */` are filtered by the WAF. We also have the logical operators `and` and `or` filtered, so there is no immediate "easy" solution by adding an extra clause to the password check. I started reading up on the sqlite documentation for some different logical operators, until I came across "IS NOT"

I read [here](https://sqlite.org/lang_expr.html) 

"The IS and IS NOT operators work like = and != except when one or both of the operands are NULL. In this case, if both operands are NULL, then the IS operator evaluates to 1 (true) and the IS NOT operator evaluates to 0 (false). If one operand is NULL and the other is not, then the IS operator evaluates to 0 (false) and the IS NOT operator is 1 (true). It is not possible for an IS or IS NOT expression to evaluate to NULL. Operators IS and IS NOT have the same precedence as =."

so I came up with the injection for the password field as follows

`' is not '1`

note how I design such that quotes in the original query are closed properly
giving a total query of 

`SELECT username, password FROM users WHERE username='ad'||'min' AND password='' is not '1'`

so, I'm still not 100% sure on the order this query resolves, but I _think_ password='' resolves as NULL and from the above excerpt we see

"If one operand is NULL and the other is not, then the IS operator evaluates to 0 (false) and the IS NOT operator is 1 (true)."

`NULL is not '1' = true`

So that's why this works :)

picoCTF{0n3_m0r3_t1m3_9605a246c21764e7691ca04679ad321a}

The same query works on Web Gauntlet 3

picoCTF{k3ep_1t_sh0rt_68847fdd50e1430d80990b518fac4edb}