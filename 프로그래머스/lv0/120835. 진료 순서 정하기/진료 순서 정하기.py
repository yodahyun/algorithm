def solution(emergency):
    result = []
    
    sort = sorted(emergency, reverse=True)
    for k, v in enumerate(emergency):
        for ek, ev in enumerate(sort):
            if ev == v:
                result.append(ek+1)
    return result
    
    