def solution(money):
    answer = []
    # divmod(a,b) -> a:몫 b:나머지
        
    cnt,charge = divmod(money, 5500)
    
    answer =[cnt, charge] 
    
    return answer