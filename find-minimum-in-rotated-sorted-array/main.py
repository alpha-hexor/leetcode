def solution(nums:list)->int:
    res = nums[0]
    low = 0
    high = len(nums)-1

    while low<=high:
        """
        check if nums is sorted or not
        if sorted then the min value is nums[low]
        """
        if nums[low] < nums[high] :
            res = min(res,nums[low])
            break
        mid = (low + high)//2
        res = min(res,nums[mid])

        #if mid in left portion then search the righ
        if nums[mid] >= nums[low]:
            low = mid +1
        else:
            high = mid -1
    return res

print(solution(nums = [3,4,5,1,2]))

