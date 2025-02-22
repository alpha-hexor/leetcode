def solution(nums:list,target:int)->int:
    low = 0
    high = len(nums)-1

    while low<=high:
        mid = (low+high)//2

        if nums[mid] == target:
            return True

        #check in left sorted array
        if nums[low] < nums[mid]:
            #check if target is in range low<=target<mid

            if nums[low]<=target<nums[mid]:
                high = mid -1
            else:
                low = mid+1
        
        #right sorted array
        elif nums[low] > nums[mid]:
            #check if target in range mid < target <= high
            if nums[mid] < target <= nums[high]:
                low = mid +1
            else:
                high = mid -1

        else:
            low +=1

    return False


print(solution(nums = [2,5,6,0,0,1,2], target = 0))
