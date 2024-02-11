'''
Question: "Reverse a String"

Problem Statement: Write a function that takes a string as input and returns the string reversed.

Example:

Input: "hello"
Output: "olleh"
At first glance, this problem seems straightforward and can be solved using a simple loop or even built-in language features. However, to add a layer of complexity and dive into intermediate-level reasoning, let's consider the following constraints and optimizations:

Memory Efficiency: Can you reverse the string in-place, using O(1) extra memory? This means not creating a copy of the string but modifying the original one.

Time Complexity: Analyze the time complexity of your solution. Is it the most efficient way to reverse a string?

Unicode and Special Characters: How does your solution handle Unicode characters or special cases like emojis or characters from various languages?

Immutable Strings: In some programming languages, strings are immutable (cannot be changed once created). How would you handle this scenario efficiently?

Recursive Solution: Can you implement a recursive solution for this problem? Discuss the pros and cons of a recursive approach compared to an iterative one.
'''

def reverseString(input_string : str) -> str: 
    ret = input_string
    
    return ret