'''
Problem: "Balanced Parentheses"

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''



def isNotBracket(char) -> bool:
    brackets = ['[', ']', '(', ')', '{', '}',]
    return char not in brackets

def main(string):
    bracketLst = []
    bracketPairs = {')': '(', '}': '{', ']': '['}

    for char in string:
        if isNotBracket(char):
            continue
        elif char in '({[':
            bracketLst.append(char)
        else:
            if not bracketLst or bracketPairs[char] != bracketLst.pop():
                return False
    
    return len(bracketLst) == 0

main('[[]]')