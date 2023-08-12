#Define Funnction
def plusMinus(arr):
    #Set the variable
    positive = 0
    negative = 0
    zero = 0
    
    #Count how many positive, negative, and zero number inside the parameter array
    for num in arr:
        if num>0:
            positive+=1
        elif num<0:
            negative+=1
        else:
            zero+=1
    
    print((positive/len(arr)))
    print((negative/len(arr)))
    print((zero/len(arr)))