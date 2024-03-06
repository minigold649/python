t = 126
a = 0.54
for i in range(30):
    t += a
    a += 0.06
print(f"{t}만{a}")