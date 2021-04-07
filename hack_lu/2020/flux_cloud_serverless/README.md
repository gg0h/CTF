### FluxCloud Serverless

```
To host stuff like our website, we developed our own cloud because we do not trust the big evil corporations! Of course we use cutting edge technologies, like serverless. Since we know what we are doing, it is totally unhackable. If you want to try, you can check out the demo and if you can access the secret, you will even get a reward :)

Note: This version of the challenge contains a bypass that has been fixed in FluxCloud Serverless 2.0.

https://serverless.cloud.flu.xxx
```

in app.js we see the endpoint to get the flag 

```js
router.get('/flag', (req, res) => {
    res.send(FLAG).end();
});
```


but the is a Web application filter (WAF) preventing us from simply accessing it with the path parameter `/flag`

blacklisted strings:
```js
const badStrings = [
    'X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*',
    'woyouyizhixiaomaol',
    'conglaiyebuqi',
    'UNION',
    'SELECT',
    'SLEEP',
    'BENCHMARK',
    'alert(1)',
    '<script>',
    'onerror',
    'flag',
];
```

first thing I thought? try uppercase since the filter is not case sensitive

and it worked: flag{ca$h_ov3rfl0w}
