def solution(d, budget):
    d.sort()
    answer = 0
    for depart in d:
        if (budget - depart >= 0):
            budget -= depart
            answer +=1
        else:
            break
    return answer