#7

A=input("siyahini daxil edin: ").split()
netice=0
cem=0
for x in A:
    cem+=int(x)
netice=cem/len(A)
print(netice)