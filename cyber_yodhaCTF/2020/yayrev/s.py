import string


m = {permutation: chr(permutation.islower() and ((ord(permutation) - 84) % 26) + 97
                        or permutation.isupper() and ((ord(permutation) - 52) % 26) + 65
                        or ord(permutation)) for permutation in string.printable} 

dcoded = "".join([m[i] for i in "lgUBAJu0n_y3tRaQ-C"])

first = dcoded[:5]
second = dcoded[5:]

print(second + first)