#define function
def miniMaxSum(arr):
    #sort array because we need to know the number order
    new_arr = sorted(arr)

    #Set the variable
    min_sum = 0
    max_sum = 0

    #Using loop to get the minimum total
    #Because the array is sorted, so the minimum sum is the total from number 1 position until the n-1 position
    for i in range(len(new_arr)-1):
        min_sum+=new_arr[i]
    
    #Using loop to get the maximum total
    #For the maximum sum we just need count from the number 2 position until the n position
    for i in range(1,len(new_arr)):
        max_sum+=new_arr[i]
    
    return print(str(min_sum)+" "+str(max_sum))