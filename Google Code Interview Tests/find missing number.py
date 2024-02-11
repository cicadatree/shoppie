'''
Problem: "Find the Missing Number in a Sequence"

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array. Your algorithm should run in linear time complexity (O(n)) and use constant extra space complexity (O(1)).

Example 1:
Input: [3, 0, 1]
Output: 2

Example 2:
Input: [0, 1]
Output: 2

Example 3:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:

The array may not be sorted.
You can assume that the array contains unique numbers.
'''    

n = 10
removed_index = 6
array = [i for i in range(1, n+1) if i != removed_index]

def compareSums(full, starting):
    print(sum(full)-sum(starting))
    return (sum(full) - sum(starting))

def checkMissingNo(array, n):
    total_sum = n * (n+1) // 2
    array_sum = sum(array)
    missing_number = total_sum - array_sum
    return missing_number

checkMissingNo(array, n)




