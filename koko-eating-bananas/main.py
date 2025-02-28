def solution(piles:list,h:int)->int:

    def is_solution(ans:int)->int:
        hour = 0
        for i in piles:
            if i <= ans:
                hour +=1
            else:
                r = (i//ans)+1 if (i%ans) else (i//ans)
                hour +=r
        return hour

    low = 1
    high = max(piles)
    ans = -1

    #check a number which lies between piles
    while low <= high:
        mid = (low + high)//2
        sol = is_solution(mid)
        if sol <= h:
            ans = mid
            #search in the left if any less value possible
            high = mid -1
        elif sol > h:
            low = mid +1
    return ans

print(solution(piles = [3,6,7,11], h = 8))
print(solution(piles = [30,11,23,4,20], h = 5))
print(solution(piles = [30,11,23,4,20], h = 6))
