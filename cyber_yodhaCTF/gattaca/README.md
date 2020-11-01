### Gattaca

we are given cipher 

`GTTAAAGTTTTCGGT{ACGACTTGCCCTACCTCTTTTATAGTGTCAACTAGGTGCGCATCCAGAATAACCACGATAACCTCTATAAAAACTCTGTCAATATTGTCTCGA}`

I recognised it being some sort of DNA encoding.

after hours of searching I found the correct conversion table

```python
s = "GTT AAA GTT TTC GGT ACG ACT TGC CCT ACC TCT TTT ATA GTG TCA ACT AGG TGC GCA TCC AGA ATA ACC ACG ATA ACC TCT ATA AAA ACT CTG TCA ATA TTG TCT CGA"

sl = s.split(" ")
print(s)

conversion = {
    "CGA": "A",
    "CCA": "B",
    "GTT": "C",
    "TTG": "D",
    "GGC": "E",
    "GGT": "F",
    "TTT": "G",
    "CGC": "H",
    "ATG": "I",
    "AGT": "J",
    "AAG": "K",
    "TGC": "L",
    "TCC": "M",
    "TCT": "N",
    "GGA": "O",
    "GTG": "P",
    "AAC": "Q",
    "TCA": "R",
    "ACG": "S",
    "TTC": "T",
    "CTG": "U",
    "CCT": "V",
    "CCG": "W",
    "CTA": "X",
    "AAA": "Y",
    "CTT": "Z",
    "ATA": "_",
    "TCG": ",",
    "GAT": ".",
    "GCT": ":",
    "ACT": "0",
    "ACC": "1",
    "TAG": "2",
    "GCA": "3",
    "GAG": "4",
    "AGA": "5",
    "TTA": "6",
    "ACA": "7",
    "AGG": "8",
    "GCG": "9",
    "CCC": " ",
}

print("".join([conversion[i] for i in sl]))
```

CYCTF{S0LV1NG_PR08L3M5_1S_1N_Y0UR_DNA}

for strange reason spaces are needed instead of underscore

CYCTF{S0LV1NG PR08L3M5 1S 1N Y0UR DNA}