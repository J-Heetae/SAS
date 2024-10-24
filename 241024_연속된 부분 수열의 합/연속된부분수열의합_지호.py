# def solution(sequence, k):
#     answer = []
#     for i in range(len(sequence)):
#         sum=0
#         for j in range(i,(len(sequence))):
#             sum+=sequence[j]
#             if sum==k:
#                 answer.append([i,j])
#             elif sum>k :
#                 continue
#     answer.sort(key=lambda x:x[1]-x[0])
#     return answer[0]

#투포인터 알고리즘
def solution(sequence, k):
    answer = []
    left = 0
    sum = 0

    for right in range(len(sequence)):
        sum += sequence[right]

        while sum > k and left <= right:
            sum -= sequence[left]
            left += 1

        if sum == k:
            answer.append([left, right])

    answer.sort(key=lambda x: x[1] - x[0])
    return answer[0]