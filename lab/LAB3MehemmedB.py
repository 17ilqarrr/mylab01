#12
#İki ölçülü A(n,n) ədədi massivinin baş dioqonal elementlərinin cəmini hesablayan alqoritm tərtib etməli.
import math,random
n=4
a=[]
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(random.randint(1,3))

def diognal_find(g):
    diognal_sum = 0
    for x in range(len(g)):
        diognal_sum+=g[x][x]
    return diognal_sum
ret=diognal_find(a)
print(ret)
print(a)
        
    