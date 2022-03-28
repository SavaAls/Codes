n=int(input("Number = ")) # 1 проверь себя(это писать не нужно), частично сделанная
k=2
while k*k<=n:
    if n%k==0:
        if k%2==0:
            print(k)
        m=n//k
        if m%2==0 and m!=k:
            print(m)

    k+=1

