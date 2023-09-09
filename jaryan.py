dimension = list(map(int,input().split()))
mokhtasat = tuple(map(int,input().split()))
lis=[]
for _ in range(dimension[0]):
    m = list(map(int,input().split()))
    lis.append(m)
case = [mokhtasat]

is_end = False

def jaryan(position):

    global is_end

    x, y = position[0], position[1]

    # base
    for i in case:
        if x == 0 or y == 0 or x == dimension[0] - 1 or y == dimension[1] - 1:
            if i == case[0]:
                continue
            if x - 1 >= 0 and lis[x][y] > lis[x - 1][y]:
                continue
            if x + 1 < dimension[0] and lis[x][y] > lis[x + 1][y]:
                continue
            if y - 1 >= 0 and lis[x][y] > lis[x][y - 1]:
                continue
            if y + 1 < dimension[1] and lis[x][y] > lis[x][y + 1]:
                continue
            is_end = True
    
    # up (x - 1, y)
    if x - 1 >= 0 and lis[x][y] > lis[x - 1][y]:
        if (x - 1, y) not in case:
            case.append((x - 1, y))
        jaryan((x - 1, y))
    # right (x, y + 1)
    if y + 1 < dimension[1] and lis[x][y] > lis[x][y + 1]:
        if (x, y + 1) not in case:
            case.append((x, y + 1))
        jaryan((x, y + 1))
    # down (x + 1, y)
    if x + 1 < dimension[0] and lis[x][y] > lis[x + 1][y]:
        if (x + 1, y) not in case:
            case.append((x + 1, y))
        jaryan((x + 1, y))
    # left (x, y - 1)
    if y - 1 >= 0 and lis[x][y] > lis[x][y - 1]:
        if (x, y - 1) not in case:
            case.append((x, y - 1))
        jaryan((x, y - 1))


jaryan(mokhtasat)

if is_end:
    print(*sorted(case), sep='\n')
else:
    print('False')
