#the maximum subarray problem
import time
import numpy as np
import tracemalloc

start = time.time()
tracemalloc.start()

#array example from the book
A = np.random.randint(-99, 99, (1000))
#function to find the maximum contiguous subarray
def FindMaxSubarray(A, size): 
 
    maxSum = -999 #set very small value
    
    #define defaults for variables
    currentMaxSum = 0
    start = 0
    end = 0
    s = 0
 
    for i in range(0, size) : #runs through the whole array
 
        currentMaxSum += A[i] #adds the current index to the find the current max sum
 
        if maxSum < currentMaxSum : #if the former sum was lower than the current sum
            maxSum = currentMaxSum #set the current sum to max so far
            start = s #set the start index to the current subarrays start index as defined in line 28
            end = i #set the end index of the subarray to the current index
 
        if currentMaxSum < 0 :
            currentMaxSum = 0 #resets the sum of the current index as it was negative
            s = i+1 #sets a new starting index for the next possibly better subarray

    return start, end, maxSum
 
#execute the function to find the subarray
startIndex, endIndex, subarraySum = FindMaxSubarray(A,len(A))

#print the subarray, its sum and the starting and ending index.
print ("The subarray is", A[startIndex:endIndex+1], "and has a sum of", subarraySum)

#execution time
end = time.time()
print("Execution time: ", end - start)

#memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6} MB and the peak was {peak / 10**6} MB")
tracemalloc.stop()