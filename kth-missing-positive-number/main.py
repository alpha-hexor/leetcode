def solution(arr:list,k:int)->int:
    """
    Notes:
    No. of missing element at i th position is arr[i]-i-1
    Result-> after binary search return right + k +1 
    """

    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high)//2 

        """
        check no. of missing elments at mid
        if no. is less than k then we need more elements so move low to mid+1 
        """
        num = abs(arr[mid] - (mid +1))

        if num <k:
            low = mid +1 
        else:
            high = mid -1
    
    return high+k+1 

print(solution(arr = [2,3,4,7,11], k = 5))

print(solution(arr = [1,2,3,4], k = 2))
