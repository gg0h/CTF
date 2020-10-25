### FluxCloud Serverless 2

```
To host stuff like our website, we developed our own cloud because we do not trust the big evil corporations! Of course we use cutting edge technologies, like serverless. Since we know what we are doing, it is totally unhackable. If you want to try, you can check out the demo and if you can access the secret, you will even get a reward :)

Note: This is the fixed version of FluxCloud Serverless.
```

the waf has been update to recursively remove URI encodings and is case insensitive 

```js
const badStrings = [
    /X5O!P%@AP\[4\\PZX54\(P\^\)7CC\)7\}\$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!\$H\+H\*/i,
    /woyouyizhixiaomaol/i,
    /conglaiyebuqi/i,
    /UNION/i,
    /SELECT/i,
    /SLEEP/i,
    /BENCHMARK/i,
    /alert\(1\)/i,
    /<script>/i,
    /onerror/i,
    /flag/i,
];

function checkRecursive(value) {
    // don't get bypassed by double-encoding
    const hasPercentEncoding = /%[a-fA-F0-9]{2}/i.test(value);
    if (hasPercentEncoding) {
        return checkRecursive(decodeURIComponent(value));
    }

    // check for any bad word
    for (const badWord of badStrings) {
        if (badWord.test(value)) {
            return true;
        }
    }
    return false;
}
```

I could not figure out how to bypass both the percent regex and WAF word list, so i didn't end up solving this one

