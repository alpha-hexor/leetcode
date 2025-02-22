def solution(nums:list)->int:
    """
    logic:
        if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
            return num
        else:
            check the odd sized array and shift pointer accordingly
    """
    low = 0
    high = len(nums) -1
    while low <= high:
        mid = (low + high) //2
        if (mid+1 == len(nums) or nums[mid] != nums[mid +1]) and (mid -1 <0 or nums[mid] != nums[mid-1]):
            return nums[mid]

        size = (mid +1) if nums[mid] == nums[mid+1] else mid
        if size %2: #if odd
            low = mid +1
        else:
            high = mid-1
print(solution(nums = [1,1,2,2,3]))
print(solution(nums = [3,3,7,7,10,11,11]))
