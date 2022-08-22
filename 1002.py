l = int(input())
a = list(range(l))
for i in range(l):
    a[i]=list(map(int,input().split()))
for i in range(l):
    b = a[i]
    d = (b[0]-b[3])**2 + (b[1]-b[4])**2
    r1 = (b[2]-b[5])**2
    r2 = (b[2]+b[5])**2
    if d==0 and r1 == 0:
        print(-1)
    elif d<r2 and r1<d :
        print(2)
    elif d == r2 or d == r1:
        print(1)
    else:
        print(0)
