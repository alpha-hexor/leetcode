def solution(nums:list,target:int)->int:

    low = 0
    high = len(nums)-1

    while low<=high:
        mid = (low+high)//2

        if nums[mid] == target:
            return mid

        #left sorted array
        if nums[low] <= nums[mid]:

            #check if target doesn't exist in left array
            if target < nums[low] or target > nums[mid]:
                
                low = mid +1 #shift the low pointer to the right array

            else:
                high = mid -1

        else: #check the right sorted array

            if target > nums[high] or target < nums[mid]:

                high = mid -1 #shift it to the right array
            else:
                low = mid +1
    return -1


print(solution(nums = [4,5,6,7,0,1,2], target = 3))

