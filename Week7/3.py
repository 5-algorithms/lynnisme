import collections
def solution(participant, completion):
    part = collections.Counter(participant)
    comp = collections.Counter(completion)
    print(part - comp)
    return 1