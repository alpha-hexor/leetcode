def spiral_matrix(matrix:list)->list:
    res = []

    l,r = 0, len(matrix[0])
    t,b = 0, len(matrix)

    #condition check
    while l<r and t<b:
        #get element of top row
        for i in range(l,r):
            res.append(matrix[t][i])

        #after top row is done increatse top
        t +=1

        #get elements of right column
        for i in range(t,b):
            res.append(matrix[i][r-1])

        #after right column is done decrease the value of right
        r -= 1

        #get elements of bottom row
        for i in range(r-1,l-1,-1):
            res.append(matrix[b-1][i])
        
        #after bottom row is done decrease bottom row
        b -=1

        #elements of left coloumn
        for i in range(b-1,t-1,-1):
            res.append(matrix[i][l])
        l+=1

    return res

print(spiral_matrix(matrix = [[1,2,3],[4,5,6],[7,8,9]]))



