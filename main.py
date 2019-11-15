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

print('*******'*10)


def entropy(*args):

    if (len(args) == 1):
        # print('in args1')
        x = args[0]

        size = len(x)
        pos = 0
        neg = 0

        for i in range(size):
            if (x[i] == 0):
                neg += 1
            else:
                pos += 1
        e = abs((math.log((pos/size),2) * (pos/size)) + (math.log((neg/size),2) * (neg/size)))
        return e

    elif(len(args)==2):
        # print('in args2')
        pos = args[0]
        neg = args[1]

        size = pos + neg
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

def getSubset(*args):

    if (len(args) == 2):
        colnum = args[0]
        flag = args[1]

        subsetReturn = []

        size = len(colnum)
        y = getColumn(3)

        for i in range (size):
            if (colnum[i] == flag) and (y[i] == flag):
                subsetReturn.append(1)
            elif (colnum[i] == flag) and (y[i] != flag):
                subsetReturn.append(0)
        return subsetReturn

    # elif (len(args) == 4):
    #     colnum1 = args[0]
    #     colnum2 = args[1]
    #     flag1 = args[2]
    #     flag2 = args[3]
    #
    #     subsetReturn = []
    #
    #     size = len(colnum1)
    #
    #     y = getColumn(3)
    #
    #     for i in range(size):
    #         if (colnum1[i] == flag1)  and (colnum2[i] == flag2) and (y[i] == flag2):
    #             subsetReturn.append(1)
    #         elif (colnum1[i] == flag1) and (colnum2[i] == flag1) and (y[i] != flag1):
    #             subsetReturn.append(0)
    #
    #     return subsetReturn



def informationGain(x,y):
    return x-y

def recursiveFunction(cand, entropySystem, i):
        best = []
        print(f'col: {i} boolean: 1')
        temp = getSubset(cand,1)
        pos1,neg1 = getTrueFalse(temp)
        entropy1 = entropy(pos1,neg1)
        print(f'pos: {pos1} \t neg: {neg1}')
        print(f'entropy: {entropy1}')

        print(f'col: {i} boolean: 0')
        temp = getSubset(cand,0)
        pos2,neg2 = getTrueFalse(temp)
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
        return informationG

def run2():
    tree = [-1]*25
    #get entropy of whole system

    entropySystem = getColumn(col-1)
    entropySystem = entropy(entropySystem)
    print()
    print(f'entropy of system: {entropySystem}')
    print()

    #now get entropy of each attribute


    best = []
    for i in range(col-1):
        cand = getColumn(i)
        best.append(recursiveFunction(cand,entropySystem,i))
    pickNode = -1
    nodeIndex = -1

    #find the candidate that had the highest information gain
    for i in range(len(best)):
        if (best[i] > pickNode):
            pickNode = best[i]
            bestInfo = pickNode
            nodeIndex = i

    print(f'best node, column: {nodeIndex}')
    #set
    totalColNum = col - 1
    tree[0] = nodeIndex
    cand = getColumn(nodeIndex)
    entropy1 = -1
    entropy2 = -1
    i = 0
    while(entropy1 !=0 or entropy2 !=0):

    #find left
        print(f'col: {nodeIndex} boolean: 1')
        temp = getSubset(cand, 1)
        pos1,neg1 = getTrueFalse(temp)
        entropy1 = entropy(pos1, neg1)
        print(f'pos: {pos1} \t neg: {neg1}')
        print(f'entropy: {entropy1}')

    #find right
        print(f'col: {nodeIndex} boolean: 0')

        temp = getSubset(cand, 0)
        pos2, neg2 = getTrueFalse(temp)
        entropy2 = entropy(pos2, neg2)
        print(f'pos: {pos2} \t neg: {neg2}')
        print(f'entropy: {entropy2}')

        i += 1

        if(entropy1 == 0):
            tree[i] = 'yes'

        if (entropy2 == 0):
            tree[i*2] = 'no'

        # elif (entropy1 != 0):
        #     for i in range (totalColNum):
        #         for j in range(2):
        #             pass

    print('*****' * 10)
    print('stop')

    print(tree)


run2()
