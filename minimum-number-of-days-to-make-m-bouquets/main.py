def solution( bloomDay:list, m:int, k:int)->int:

    def calculate_flower(day:int)->int:
        flower = 0 
        boque = 0

        for i in bloomDay:
            #if day is valid
            if i <= day:
                flower +=1
                if flower == k:
                    #if no. of target flower reached increase boque
                    #and we need a fresh start
                    boque +=1
                    flower = 0
            else:
                #if day is not valid we need fresh start
                flower = 0
        return boque

    total_flowers = m*k
    if len(bloomDay) < total_flowers:
        return -1
    else:
        low = 1
        high = max(bloomDay)
        ans = -1

        while low <= high:
            mid = (low + high)//2
            f = calculate_flower(mid)
            print(f"mid:{mid} no.of_flower:{f}")
            if f>= m:
                ans = mid
                high = mid -1
            else:
                low = mid +1
        return ans
print(solution( bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))
print(solution(bloomDay = [1,10,3,10,2], m = 3, k = 1))

