def solution(str1, str2):
    answer = 0
    list1 = [v.lower() for v in [str1[i] + str1[i+1] for i in range(len(str1) - 1)] if v.isalpha()]
    list2 = [v.lower() for v in [str2[i] + str2[i+1] for i in range(len(str2) - 1)] if v.isalpha()]
    if not list1 and not list2:
        return 1 * 65536
    temp1 = list1.copy()
    hop = list1.copy()

    for i in list2:
        if i not in temp1:
            hop.append(i)
        else:
            temp1.remove(i)
    
    a = list1.copy()
    b = list2.copy()
            
    kyo = []
    for i in b:
        if i in a:
            a.remove(i)
            kyo.append(i)
            
    print(list1, list2)
    print(hop, kyo)
    
    return int(len(kyo) / len(hop) * 65536)
