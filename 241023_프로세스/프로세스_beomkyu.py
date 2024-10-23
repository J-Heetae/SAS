def solution(priorities, location):
    answer = 0
    priList = [(idx, v) for idx, v in enumerate(priorities)]
    print(priList)
    while priList:
        pop = priList.pop(0)
        if any(pop[1] < v[1] for v in priList):
            priList.append(pop)
        else:
            answer += 1
            if pop[0] == location:
                return answer
    return answer
