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

row = len(data)
col = len(data[0])
for i in range(row):
    str = ""
    for j in range(col):
        str += (data[i][j]).__str__()
        str += ' '
    print(str)
