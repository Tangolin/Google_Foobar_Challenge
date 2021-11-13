def solution(s):
    s = list(s)
    positions = [index for index, minion in enumerate(s) if minion == '>']
    salutes = sum([s[index:].count('<') for index in positions])
    
    return salutes * 2
