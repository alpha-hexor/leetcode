def spiral_to_matrix(n:int)->list:
    nums = list(range(1,(n*n)+1))
    res = []
    
    for _ in range(n):
        res.append([0]*n)

    left = 0
    right = n

    top =0
    bottom = n
    i = 0
    while left<right and top<bottom:
        #fill out the top row
        for index in range(left,right):
            res[top][index] = nums[i]
            i+=1
        top +=1

        #fill out the right row
        for index in range(top,bottom):
            res[index][right-1] = nums[i]
            i+=1
        right -=1
        
        if not(left<right and top<bottom):
            break

        #fill out the bottom row
        for index in range(right-1,left-1,-1):
            res[bottom-1][index] = nums[i]
            i+=1
        bottom -=1

        #fill out the left column
        for index in range(bottom-1,top-1,-1):
            res[index][left] = nums[i]
            i+=1
        left +=1

    print(res)


spiral_to_matrix(n=3)
