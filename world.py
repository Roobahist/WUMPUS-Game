def makeworld():
    size = int(input('Enter Matrix Size = '))
    gold = list(map(int,input('GOLD Coordinate = ').split(',')))
    wampus_number = int(input('number of WAMPUSs = '))
    wampus_coordinates = []
    for i in range(wampus_number):
        wampus_coordinate = list(map(int,input('WAMPUS'+str(i)+' Coordinate = ').split(',')))
        wampus_coordinates.append(wampus_coordinate)
    pit_number = int(input('number of PITs = '))
    pit_coordinates = []
    for i in range (pit_number):
        pit_coordinate = list(map(int,input('PIT'+str(i) +' Coordinate = ').split(',')))
        pit_coordinates.append(pit_coordinate)

    Matrix = []
    for i in range (size):
        row = []
        for j in range (size):
            cell_data = {
                'A' : 0 ,
                'G' : 0 ,
                'P' : 0 ,
                'B' : 0 ,
                'W' : 0 ,
                'S' : 0 ,
            }
            row.append(cell_data)
        Matrix.append(row)

    # A
    Matrix[0][0]['A'] = 1

    # G
    Matrix[gold[0]][gold[1]]['G'] = 1

    # W
    for i in range(len(wampus_coordinates)):
        Matrix[wampus_coordinates[i][0]][wampus_coordinates[i][1]]['W'] = 1

    # S
    for i in range (len(wampus_coordinates)):
        if wampus_coordinates[i][0]-1 >= 0 :
            Matrix[wampus_coordinates[i][0]-1][wampus_coordinates[i][1]]['S'] = 1
        if wampus_coordinates[i][0]+1 <= size-1 :
            Matrix[wampus_coordinates[i][0]+1][wampus_coordinates[i][1]]['S'] = 1    
        if wampus_coordinates[i][1]-1 >= 0 :
            Matrix[wampus_coordinates[i][0]][wampus_coordinates[i][1]-1]['S'] = 1    
        if wampus_coordinates[i][1]+1 <= size-1 :
            Matrix[wampus_coordinates[i][0]][wampus_coordinates[i][1]+1]['S'] = 1 

    # P
    for i in range(len(pit_coordinates)):
        Matrix[pit_coordinates[i][0]][pit_coordinates[i][1]]['P'] = 1

    # B
    for i in range (len(pit_coordinates)):
        if pit_coordinates[i][0]-1 >= 0 :
            Matrix[pit_coordinates[i][0]-1][pit_coordinates[i][1]]['B'] = 1
        if pit_coordinates[i][0]+1 <= size-1 :
            Matrix[pit_coordinates[i][0]+1][pit_coordinates[i][1]]['B'] = 1    
        if pit_coordinates[i][1]-1 >= 0 :
            Matrix[pit_coordinates[i][0]][pit_coordinates[i][1]-1]['B'] = 1    
        if pit_coordinates[i][1]+1 <= size-1 :
            Matrix[pit_coordinates[i][0]][pit_coordinates[i][1]+1]['B'] = 1 

    return Matrix