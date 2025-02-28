def solution(nums:int)->int:
    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low + high) //2
        """
        check if mid > mid+1 and mid > mid-1 and also check for edge cases
        like mid +1 == len(nums) and mid-1 <0
        """
        if (mid +1 == len(nums) or nums[mid] > nums[mid+1]) and (mid-1 <0 or nums[mid] > nums[mid-1]):
            return mid
        elif nums[mid] > nums[mid+1]:
            high = mid -1
        else:
            low = mid +1

print(solution(nums = [6,5,4]))
