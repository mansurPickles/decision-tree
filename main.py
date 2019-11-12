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

def averageInformation(x, s_pos, s_neg):
    s_size = s_pos + s_neg

    information = (((x[0][0] + x[0][1])/s_size) * x[0][2]) + (((x[1][0] + x[1][1])/s_size) * x[1][2])
    return information


def buildInformationMatrix(pos1,neg1,e1, pos2,neg2,e2):
    matrix = [[pos1,neg1,e1], [pos2,neg2,e2]]
    return matrix



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

def informationGain(x,y):
    return y-x

col = getColumn(0)

pos1, neg1 = getSubset(col,1)
e1 = entropy(pos1,neg1)
print('has job: yes')
print(f'pos: {pos1}')
print(f'neg: {neg1}')
print(f'entropy: {e1}')

pos2, neg2 = getSubset(col,0)
e2 = entropy(pos2,neg2)
print('has job: no')
print(f'pos: {pos2}')
print(f'neg: {neg2}')
print(f'entropy: {e2}')

M = buildInformationMatrix(pos1,neg1,e1,pos2,neg2,e2)

y = getColumn(3)
pos_s, neg_s = getSubset(y,1)
pos_n, neg_s = getSubset(y,0)
es = entropy(pos_s,neg_s)
print('system total:')
print(f'pos: {pos_s}')
print(f'neg: {neg_s}')
print(f'entropy: {es}')


informationHasJob = (averageInformation(M,pos_s, neg_s))
print(f'information(hasjob): {informationHasJob}')
print(informationGain(informationHasJob, es))


#notes for me, finished checking the first column "has job" checked all values and good to go.