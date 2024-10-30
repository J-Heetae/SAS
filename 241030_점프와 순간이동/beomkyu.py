def solution(n):
    ans = 0
    
    while n != 0:
        if n % 2 == 1:
            n -= 1
            ans += 1
        else:
            n /= 2
    return ans

## + k or 2 length
