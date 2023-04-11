def n_sum(n):
    i=1
    s=0
    while int(n/i)>0:
        s+=int((n%(i*10))/i)
        i=i*10
    return s

l = [int(x) for x in input().split()]
n = l[0]
a = l[1]
b = l[2]

w = 0
for i in range(n+1):
    s = n_sum(i)
    if s>=a and s<=b:
        w=w+i

print(w)