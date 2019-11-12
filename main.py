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

x = math.log(2,10)
print(x)




def Entropy(x):
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


def getColumn(colnum):
    col = []
    size = len(data)
    for i in range(size):
        col.append(data[i][colnum])
    return col

col = getColumn(3)
Entropy(col)