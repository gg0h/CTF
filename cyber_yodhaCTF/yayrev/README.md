### yayrev

from the output we get

```text
mac>>>[0] == "l" and
mac>>>[1] == "g" and
mac>>>[2] == "U" and
mac>>>[3] == "B" and
mac>>>[4] == "A" and
mac>>>[5] == "J" and
mac>>>[6] == "u" and
mac>>>[7] == "0" and
mac>>>[8] == "n" and
mac>>>[9] == "_" and
mac>>>[10] == "y" and
mac>>>[11] == "3" and
mac>>>[12] == "t" and
mac>>>[13] == "R" and
mac>>>[14] == "a" and
mac>>>[15] == "Q" and
mac>>>[16] == "-" and
mac>>>[17] == "C" and


vravar = "lgUBAJu0n_y3tRaQ-C"
```

from here I created a map to reverse the obfuscation step and then reordered the characters

```python
import string


m = {permutation: chr(permutation.islower() and ((ord(permutation) - 84) % 26) + 97
                        or permutation.isupper() and ((ord(permutation) - 52) % 26) + 65
                        or ord(permutation)) for permutation in string.printable} 

dcoded = "".join([m[i] for i in "lgUBAJu0n_y3tRaQ-C"])

first = dcoded[:5]
second = dcoded[5:]

print(second + first)
```

flag: Wh0a_l3gEnD-PytHON (no wrapper)