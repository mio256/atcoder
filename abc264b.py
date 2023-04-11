# h1,w1=map(int,input().split())
# m1=[input().split() for _ in range(h1)]

# h2,w2=map(int,input().split())
# m2=[input().split() for _ in range(h2)]

m1=[[1,2,3],[4,5,6],[7,8,9]]
print(m1)

m2=[[1,2,3],[5,5,6],[7,8,9]]
print(m2)

while m1!=m2:
    for x in range(len(m1)):
        if m1[x]!=m2[x]:
            for i in range(len(m1)):
                del m1[i][0]
            break
    if len(m1)<len(m2):
        break
    print(m1)
    print(m2)

if m1==m2:
    print('Yes')
else:
    print('No')