def solution(my_string):
    result = 0
    my_string = list(my_string)
    
    for i in range(0, len(my_string)):
        if my_string[i].isdigit() == True:
            result += int(my_string[i])
    return result