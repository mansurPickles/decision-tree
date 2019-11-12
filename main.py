import math

data = [[1,1,1,0],
        [1,0,1,0],
        [1,0,0,1],
        [0,0,1,0],
        [0,0,0,1],
        [1,1,1,0],
        [1,0,1,0],
        [1,0,0,1],
        [0,0,1,0],
        [0,0,0,1]
        ]

#col 1 = has a job
#col 2 = has insurance
#col 3 = votes
#col 4 = action

row = len(data)
col = len(data[0])

for i in range(row):
    str = ""
    for j in range(col):
        str += (data[i][j]).__str__()
        str += ' '
    print(str)






def entropy(x):
    size = len(x)
    pos = 0
    neg = 0

    for i in range(size):
        if (x[i] == 0):
            neg += 1
        else:
            pos += 1

    print(f'pos {pos}')
    print(f'neg {neg}')
    print(f'total {size}')


    e = abs((math.log((pos/size),2) * (pos/size)) + (math.log((neg/size),2) * (neg/size)))
    return e

def entropy(pos,neg):
    size = pos + neg
    e = abs((math.log((pos/size),2) * (pos/size)) + (math.log((neg/size),2) * (neg/size)))
    return e

def average_Information(x, s_pos, s_neg):
    s_size = s_pos+s_neg
    size = len(x)
    pos = 0
    neg = 0
    entropoy_system = abs((math.log((s_pos/s_size),2) * (s_pos/s_size)) +
                          (math.log((s_neg/s_size),2) * (s_neg/s_size)))

    for i in range(size):
        if (x[i] == 0):
            neg += 1
        else:
            pos += 1



def getColumn(colnum):
    col = []
    size = len(data)
    for i in range(size):
        col.append(data[i][colnum])
    return col

def getSubset(colnum, flag):
    pos = 0
    neg = 0
    size = len(colnum)
    y = getColumn(3)

    for i in range (size):
        if (colnum[i] == flag) and (y[i] == flag):
            pos += 1
        elif (colnum[i] == flag) and (y[i] != flag):
            neg += 1

    # flag set to true, return pos/neg
    if (flag == 1):
        return pos, neg

    #flag set to false, return neg/pos
    else:
        return neg,pos

col = getColumn(0)

pos, neg = getSubset(col,1)
e = entropy(pos,neg)
print('has job: yes')
print(f'pos: {pos}')
print(f'neg: {neg}')
print(f'entropy: {e}')

pos, neg = getSubset(col,0)
e = entropy(pos,neg)
print('has job: no')
print(f'pos: {pos}')
print(f'neg: {neg}')
print(f'entropy: {e}')

