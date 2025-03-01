def solution(weights:list, days: int)->int:
    def calculate_days(target_weight:int)->int:
        """
        helper function to calculate days for a specific weight
        """
        day = 1 #minimum 1 day is needed
        sum_weight = 0

        for i in weights:
            #if sum_weight is greater than target weight
            #we need to restart
            if sum_weight + i  > target_weight:
                #need 1 more day
                day += 1
                sum_weight = 0
            sum_weight +=i

        return day

    low = max(weights) #we should atleast try with maximum weight possible
    high = sum(weights)
    ans = -1

    if days == 1:
        return sum(weights)
    while low <=high:
        mid = (low + high)//2
        d = calculate_days(mid)
        if d <= days:
            #colud be a possible solution
            ans = mid

            #check if it is possible for lesser value
            high = mid -1
        else:
            low = mid +1
    return ans

print(solution(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))
print(solution(weights = [3,2,2,4,1,4], days = 3))
print(solution(weights = [1,2,3,1,1], days = 4))

