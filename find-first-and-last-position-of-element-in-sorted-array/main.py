
#just two custom binary searches
def get_start_pos(nums:list,target:int)->int:
    low:int = 0
    high:int = len(nums) -1
    start = -1

    while low<=high:
        mid = (low + high)//2
        if nums[mid] == target:
            start = mid
            #check if there is more to the left
            #update the high value
            high = mid -1
        elif target > nums[mid]:
            low = mid +1
        else:
            high = mid -1
    return start


def get_end_pos(nums:list,target:int)->int:
    low:int = 0
    high:int = len(nums) -1
    end = -1

    while low<=high:
        mid = (low + high)//2
        if nums[mid] == target:
            end = mid
            #check if there is more to the right
            #update the low value
            low = mid +1
        elif target > nums[mid]:
            low = mid +1
        else:
            high = mid -1
    return end

nums=[5,7,7,8,8,10]
target = 8

print([get_start_pos(nums,target),get_end_pos(nums,target)])

