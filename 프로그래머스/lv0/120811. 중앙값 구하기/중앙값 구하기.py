def solution(array):
    answer = 0
    
    array.sort()
    
    length = len(array)
    index = (length-1)//2
    answer = array[index]
    
    return answer