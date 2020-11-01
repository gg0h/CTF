### something sw33t


```text
My sweet friend tried telling me about something on this page, but I can’t seem to find anything… Can you help me: https://cyberyoddha.baycyber.net:33001
```

implying cookies, looked there first and found this

```text
.eJyVU2tPwjAU_StLP4tsA9QR90EUxMWRQHQvNdh1d6zYDrOHZiP7746pgUhsoGna5tzTnnNvbtfoKs0YFK0R5pQVLRO4D0mK-mcnKGwg1F-j6yLOIoqlby7qP61RAClJ6HtGV_GGIQW02fz5HPVRTAmgqqqfYHixH_a5Jjuq1cXORHbtntxQY8xhn_pHuaqZB2iDLlB3-aj0HtzaASudzkQhY4P59qMucDFeJZjAESainONY4GGD6k3of9HnXJZDbbMC2Z5DvINcNKu_gwRb_AcJ925BV2mfqu1Lpf2qtLvqIflkEUjijKYKu7GG3rl5m4WmpZWebYVga4qjKhHYBnM67COwtIhwKyQ1RuKZJkh-RsnbEfUuAILfuRkCo8HY6DnqKHZtlgsM3EMM0gDnKV5AcoiFPOJc1PPLwWddE-ZNdVGnGbiodU2cpNFBfUYjKhYN3eVAJoq2Mjt3pUB4WP91utviL1X1BXD8TWE.X4ovdw.rz4sSG_k2heOMf7Cw_C6Kliw7Ms
```

after some searching discovered it is a flask cookie. I foundhow to decode [here](https://www.youtube.com/watch?v=mhcnBTDLxCI) the payload is the bit after the first .

`eJyVU2tPwjAU_StLP4tsA9QR90EUxMWRQHQvNdh1d6zYDrOHZiP7746pgUhsoGna5tzTnnNvbtfoKs0YFK0R5pQVLRO4D0mK-mcnKGwg1F-j6yLOIoqlby7qP61RAClJ6HtGV_GGIQW02fz5HPVRTAmgqqqfYHixH_a5Jjuq1cXORHbtntxQY8xhn_pHuaqZB2iDLlB3-aj0HtzaASudzkQhY4P59qMucDFeJZjAESainONY4GGD6k3of9HnXJZDbbMC2Z5DvINcNKu_gwRb_AcJ925BV2mfqu1Lpf2qtLvqIflkEUjijKYKu7GG3rl5m4WmpZWebYVga4qjKhHYBnM67COwtIhwKyQ1RuKZJkh-RsnbEfUuAILfuRkCo8HY6DnqKHZtlgsM3EMM0gDnKV5AcoiFPOJc1PPLwWddE-ZNdVGnGbiodU2cpNFBfUYjKhYN3eVAJoq2Mjt3pUB4WP91utviL1X1BXD8TWE`

the first `.` mean it is compressed so we must use zlib to decompress, we can do this in python

```python
import zlib
import base64

json = zlib.decompress(
    base64.urlsafe_b64decode(
        '.eJyVU2tPwjAU_StLP4tsA9QR90EUxMWRQHQvNdh1d6zYDrOHZiP7746pgUhsoGna5tzTnnNvbtfoKs0YFK0R5pQVLRO4D0mK-mcnKGwg1F-j6yLOIoqlby7qP61RAClJ6HtGV_GGIQW02fz5HPVRTAmgqqqfYHixH_a5Jjuq1cXORHbtntxQY8xhn_pHuaqZB2iDLlB3-aj0HtzaASudzkQhY4P59qMucDFeJZjAESainONY4GGD6k3of9HnXJZDbbMC2Z5DvINcNKu_gwRb_AcJ925BV2mfqu1Lpf2qtLvqIflkEUjijKYKu7GG3rl5m4WmpZWebYVga4qjKhHYBnM67COwtIhwKyQ1RuKZJkh-RsnbEfUuAILfuRkCo8HY6DnqKHZtlgsM3EMM0gDnKV5AcoiFPOJc1PPLwWddE-ZNdVGnGbiodU2cpNFBfUYjKhYN3eVAJoq2Mjt3pUB4WP91utviL1X1BXD8TWE==='
    ))
print(json)

{
    "Astley-Family-Members": 6,
    "family": {
        "Cynthia Astley": [{
            "description": {
                " di": {
                    " b__": "nice"
                }
            },
            "flag": {
                " di": {
                    " b__": "bm90X2V4aXN0YW50"
                }
            },
            "name": {
                " di": {
                    " b__": "Cynthia Astley"
                }
            }
        }, {
            "description": {
                " di": {
                    " b__": "nicee="
                }
            },
            "flag": {
                " di": {
                    " b__": "YmFzZTY0X2lzX3N1cHJlbWU="
                }
            },
            "name": {
                " di": {
                    " b__": "Horace Astley"
                }
            }
        }, {
            "description": {
                " di": {
                    " b__": "human"
                }
            },
            "flag": {
                " di": {
                    " b__": "flag=flag"
                }
            },
            "name": {
                " di": {
                    " b__":
                    "\\u00f9\\u00ec\\u00f9\\u00fa\\u00ec\\u00f8\\u00fb\\u00ec\\u00fd\\u00f8\\u00ec\\u00ff\\u00fa\\u00ec\\u00fe41/.2/<1/`1/42"
                }
            }
        }, {
            "description": {
                " di": {
                    " b__": "the man"
                }
            },
            "flag": {
                " di": {
                    " b__":
                    "Q1lDVEZ7MGtfMV9zZWVfeW91X21heWJlX3lvdV9hcmVfc21hcnR9"
                }
            },
            "name": {
                " di": {
                    " b__": "Rick Astley"
                }
            }
        }, {
            "description": {
                " di": {
                    " b__": "yeedeedeedeeeeee"
                }
            },
            "flag": {
                " di": {
                    " b__": "dHJ5X2FnYWlu"
                }
            },
            "name": {
                " di": {
                    " b__": "Lene Bausager"
                }
            }
        }, {
            "description": {
                " di": {
                    " b__": "uhmm"
                }
            },
            "flag": {
                " di": {
                    " b__": "bjBwZWVlZQ=="
                }
            },
            "name": {
                " di": {
                    " b__": "Jayne Marsh"
                }
            }
        }, {
            "description": {
                " di": {
                    " b__": "hihi"
                }
            },
            "flag": {
                " di": {
                    " b__": "bjBfYjB0c19oM3Iz"
                }
            },
            "name": {
                " di": {
                    " b__": "Emilie Astley"
                }
            }
        }]
    }
}
```

I tried decoding the base64 in the ouput dict one by one until I found the flag

`echo Q1lDVEZ7MGtfMV9zZWVfeW91X21heWJlX3lvdV9hcmVfc21hcnR9 | base64 -d`

CYCTF{0k_1_see_you_maybe_you_are_smart}