def solution(array, n):
    cnt = 0
    
    for a in array:
        if a == n:
            cnt = cnt+1
            
    return cnt