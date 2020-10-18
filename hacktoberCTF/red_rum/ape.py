s = ""

red_rum = []

for i in range(1, 501):
    if (i % 3 == 0) and (i % 5 == 0):
        s = "RedRum"
    elif i % 3 == 0:
        s = "Red"
    elif i % 5 == 0:
        s = "Rum"
    else:
        s = str(i)
    red_rum.append(s)

print(",".join(red_rum))
    

