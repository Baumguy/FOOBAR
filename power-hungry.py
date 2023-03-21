def solution(xs):
    neg=[]
    maximum=1
    #If there's only one panel in the array, this is its total power output.
    if len(xs)==1:
        return(str(sum(xs)))
    
    #Finds the maximum power
    for item in xs:
        #print(item)
        if item!=0:
            maximum=(maximum*item)
        #Sorts negatives numbers into a list for cases in which the maximum power would be negative.
        if item<0:
          neg.append(item)

    #If maximum power is negative, divides by the negative number closest to zero to make it a postive number again.
    if maximum<0 and len(neg)>1:
        return(str(int(maximum/max(neg))))
    
    #If maximum power is negative and there are no other negatives to make positives out of, zero is the new maximum output.
    if maximum<0 and len(neg)<=1:
        return(str(0))
    
    #If all numbers in the array are zero, returns a zero output.
    if all(number == 0 for number in xs):
        return(str(0))
        
        
    return(str(maximum))