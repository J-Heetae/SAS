import math
def solution(sequence, k):
    answer = []
    x = 0
    list_sum = 0
    min_length = math.inf
    for y in range(len(sequence)):
        list_sum += sequence[y]
        while list_sum >= k:
            if list_sum == k and min_length > y - x:
                min_length = y - x
                answer = [x, y]
            list_sum -= sequence[x]
            x += 1
    return answer
