

#using binary seach method
def get_pos(nums:list,target:int)->int:
    low:int = 0
    high:int = len(nums)-1

    floor_index:int = -1

    while low<=high:
        mid = (low+high) //2

        if nums[mid] <= target:
            floor_index = mid
            low = mid +1
        else:
            high = mid -1
    return floor_index

nums = [1,3,5,6,8]
target =7
index = get_pos(nums=nums,target=target)
if nums[index] == target:
    print(index)
elif index  == -1:
    print(len(nums))
else:
    print(index+1)

