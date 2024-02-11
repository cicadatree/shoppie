'''
Problem: "Maximum Subarray Sum"

You are given an array of integers, which can include both positive and negative numbers. Your task is to find the contiguous subarray (containing at least one number) which has the largest sum and return that sum.

For example:

For the array [-2,1,-3,4,-1,2,1,-5,4], the contiguous subarray [4,-1,2,1] has the largest sum = 6.
For the array [1], the single element 1 is the largest sum.
Consider the following points in your solution:

Think about how you can keep track of the sum as you iterate through the array.
Consider the possibility of a negative sum and how it affects the maximum sum.
'''
sample_array = [2, -3, 4, -1, -2, 1, 5, -3]

def check_neighbours(array : list, index : int, tracker : list):
    if index < 0 or index >= len(array):
        return "Invalid index"
    elif index == 0:
        if (array[index] + array[index + 1]) > 0:
            tracker.append(index)
    elif index == len(array) - 1:
        if (array[index] + array[index-1]) > 0:
            tracker.append(index)
    else:
        if array[index] + (array[index +1] + array[index - 1]) > 0:
            tracker.append(index)
    return tracker


def findMaxSum(array : list):
    tracking_list = []
    largest_value = max(array) # get the single largest int in the array
    if largest_value >= sum(array[0:len(array)-1]) and sum(array[1:len(array)]):    # next, check if sum of either of the two largest contiguous subarrays (array[0:len(array)-1] and array[1:len(array)])
        print(f"{largest_value} is the largest subarray")
        return largest_value
    else:
        for i in range(0,len(array)-1):
            listOfNonZeroSmallestSubarrays = check_neighbours(array, i, tracking_list)
    print(listOfNonZeroSmallestSubarrays)
    return True

findMaxSum(sample_array)