from collections import deque
def solution(priorities, location):
    priList = []
    for i, pri in enumerate(priorities):
        priList.append([pri,i])
    priQue = deque(priList)
   
    sum=0
    while True:
        if priQue[0][0]==max(priorities):
            if priQue[0][1]==location:
                sum+=1
                break
            else:
                sum+=1
                priorities.remove(priQue[0][0])
                priQue.popleft()
        else:
            pri,i = priQue.popleft()
            priQue.append([pri,i])

    return sum