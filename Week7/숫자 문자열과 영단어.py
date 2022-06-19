def solution(s):
    dicts = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, 
             "seven":7, "eight":8, "nine":9}
    
    answer = 0
    for key in dicts.keys():
        if (key in s):
            s = s.replace(key, str(dicts[key]))
    answer = int(s)
    return answer