T = int(input())
N=[ 0 for _ in range(T)]
K=[ 0 for _ in range(T)]
D=[ [] for _ in range(T)]
xy=[ [] for _ in range(T)]
W=[ [] for _ in range(T)]
for i in range(T):
    N[i],K[i] = map(int,input().split())
    D[i].append(list(map(int,input().split())))
    for j in range(K[i]):
        xy[i].append(list(map(int,input().split())))
    W[i]=int(input())
#print(xy)
