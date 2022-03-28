a = []
k = 10
for r in range(3):
    a.append([])
    for c in range(3):
        a[r].append(k)
        k += 1

for r in a:
    print(r)
