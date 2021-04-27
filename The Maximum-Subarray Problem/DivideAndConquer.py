#the maximum subarray problem (divide and conquer approch with recursion)
import time
import numpy as np
import tracemalloc

start = time.time()
tracemalloc.start()

#array example from the book
A = np.random.randint(-99, 99, (1000))

startIndex = 0
endIndex = len(A)-1

#recursive function to find the maximum contiguous subarray
def FindMaxSubarray(A, low, high):
    mid = (low + high) // 2  #mid index for the current array

    if high == low:    
        return low, high, A[low]  #if the current array only has one element return it

    leftLow, leftHigh, leftSum = FindMaxSubarray(A, low, mid) #make a new array (from index 0 to the current mid index) and run it through the function
    rightLow, rightHigh, rightSum = FindMaxSubarray(A, mid+1, high) #make a new array (from the current mid index to the end index) and run it through the function 

    crossLow, crossHigh, crossSum = FindMaxCrossingSubarray(A, low, mid, high) #find the maximum sum of the current mid-crossing subarray

    #return the sum (including start and end indexes) for the function with the highest sum
    if leftSum >= rightSum and leftSum >= crossSum :
        return leftLow, leftHigh, leftSum

    elif rightSum >= leftSum and rightSum >= crossSum :
        return rightLow, rightHigh, rightSum
        
    else :
        return crossLow, crossHigh, crossSum

#function to find maximum sum of mid-crossing subarrays
def FindMaxCrossingSubarray(A, low, mid, high):

    #set default values for the left side
    leftSum = -10000 
    maxLeft = 0
    total = 0                          

    #find the max sum to the left
    for i in range(mid, low-1, -1) :    #loop through the left array
        total = total + A[i]            #add current index's value to total
        if total > leftSum :            #if the current sum (total) is higher than the former sum
            leftSum = total             #set the max left sum to be equal to the current sum 
            maxLeft = i                 #set the start index to be the current index

    #set default values for the right side
    rightSum = -10000
    maxRight = 0
    total = 0        

    #find the max sum to the right         
    for j in range(mid+1, high+1) :   #loop through the right array
        total = total + A[j]        #add current index's value to total
        if total > rightSum :       #if the current sum (total) is higher than the former sum
            rightSum = total        #set the max left sum to be equal to the current sum 
            maxRight = j            #set the end index to be the current index
    
    crossarraySum = leftSum + rightSum  #combine the two sums

    return maxLeft, maxRight, crossarraySum  #return the sum (including start and end indexes)

#execute the function to find the subarray
subarrayStartIndex, subarrayEndIndex, subarraySum = FindMaxSubarray(A, startIndex, endIndex)

#print the subarray, its sum and the starting and ending index.
print ("The subarray is", A[subarrayStartIndex:subarrayEndIndex+1], "and has a sum of", subarraySum)

#execution time
end = time.time()
print("Execution time: ", end - start)

#memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6} MB and the peak was {peak / 10**6} MB")
tracemalloc.stop()