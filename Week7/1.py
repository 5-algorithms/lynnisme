# 최대 공약수 계산 모듈
from math import gcd

def solution(n, m):
    answer = []
    answer.append(gcd(n,m))
    answer.append(n*m//answer[0])
    return answer