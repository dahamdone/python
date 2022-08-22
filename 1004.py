l = int(input())
case = list(range(l))
coor = list(range(l))
ll = list(range(l))
for i in range(l):
    coor[i] = list(map(int,input().split()))
    ll[i] = int(input())
    case[i]=list(range(ll[i]))
    for j in range(ll[i]):
        case[i][j]=list(map(int,input().split()))
#print(coor)
for i in range(l):
    count = 0
    for j in range(ll[i]):
        if (coor[i][0]-case[i][j][0])**2+(coor[i][1]-case[i][j][1])**2<case[i][j][2]**2 and (coor[i][2]-case[i][j][0])**2+(coor[i][3]-case[i][j][1])**2>case[i][j][2]**2:
            count = count+1
        elif (coor[i][0]-case[i][j][0])**2+(coor[i][1]-case[i][j][1])**2>case[i][j][2]**2 and (coor[i][2]-case[i][j][0])**2+(coor[i][3]-case[i][j][1])**2<case[i][j][2]**2:
            count = count+1
    print(count)
