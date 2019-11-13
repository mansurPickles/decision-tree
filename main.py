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




def entropy(*args):

    if (len(args) == 1):
        print('in args1')
        x = args[0]

        size = len(x)
        print(f'size {size}')

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

    elif(len(args)==2):
        # print('in args2')

        pos = args[0]
        neg = args[1]

        size = pos + neg
        # print(f'size: {size}')
        # print(f'pos: {pos}')
        # print(f'neg: {neg}')

        if (pos == 0 or neg == 0):
            return 0

        else:
            e = abs((math.log((pos / size), 2) * (pos / size)) + (math.log((neg / size), 2) * (neg / size)))
            return e

def getTrueFalse(x):
    size = len(x)

    pos = 0
    neg = 0

    for i in range(size):
        if (x[i] == 0):
            neg += 1
        else:
            pos += 1

    return pos,neg


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
    return x-y



def run():
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
    print('\n')


    #notes for me, finished checking the first column "has job" checked all values and good to go.

def run2():
    #get entropy of whole system
    entropySystem = getColumn(col-1)
    entropySystem = entropy(entropySystem)
    print(f'entropy of system: {entropySystem}')

    #now get entropy of each attribute
    best = []

    for i in range(col-1):
        cand = getColumn(i)
        print(f'col: {i} boolean: 1')
        pos1,neg1 = getSubset(cand,1)
        entropy1 = entropy(pos1,neg1)
        print(f'pos: {pos1} \t neg: {neg1}')
        print(f'entropy: {entropy1}')

        print(f'col: {i} boolean: 0')
        pos2,neg2 = getSubset(cand,0)
        entropy2 = entropy(pos2,neg2)
        print(f'pos: {pos2} \t neg: {neg2}')
        print(f'entropy: {entropy2}')

        #now calculate the average entropy
        pos_s,neg_s = getTrueFalse(getColumn(col-1))
        M = buildInformationMatrix(pos1,neg1,entropy1, pos2, neg2,entropy2)
        information = averageInformation(M,pos_s,neg_s)
        print(f'average information: {information}')

        #calculate information gain
        informationG = informationGain(entropySystem,information)
        best.append(informationG)
        print(f'information gain: {informationG}')
        print('\n')

    pickNode = -1
    nodeIndex = -1

    for i in range(len(best)):
        if (best[i] > pickNode):
            pickNode = best[i]
            nodeIndex = i
    print(f'best node, column: {nodeIndex}')

    cand = getColumn(nodeIndex)

    print(f'col: {nodeIndex} boolean: 1')
    pos1, neg1 = getSubset(cand, 1)
    entropy1 = entropy(pos1, neg1)
    print(f'pos: {pos1} \t neg: {neg1}')
    print(f'entropy: {entropy1}')

    print(f'col: {nodeIndex} boolean: 0')
    pos2, neg2 = getSubset(cand, 0)
    entropy2 = entropy(pos2, neg2)
    print(f'pos: {pos2} \t neg: {neg2}')
    print(f'entropy: {entropy2}')


    print('*****' * 10)
    print('stop')



run2()