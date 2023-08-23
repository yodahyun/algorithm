def solution(start, end_num):
    answer = []
    
    #for i in range(start, end_num-1, -1)
    while start >= end_num:
        answer.append(start)
        start-=1
        
    return answer