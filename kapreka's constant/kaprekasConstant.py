
userInput = input("input a 4 digit number with at least two non-repeating numbers: ")
userInput = str(userInput)
repCounter = 0

def kaprekasConstant(number, repCounter):
    sortedDescending = sorted(number,reverse=True)
    sortedAscending = sorted(number)
    sortedDescendingJoined = int("".join(sortedDescending))
    sortedAscendingJoined = int("".join(sortedAscending))
    res = sortedDescendingJoined - sortedAscendingJoined
    repCounter = repCounter + 1
    if res != 6174:
        kaprekasConstant(str(res), repCounter)
    else:
        print(res,", ",repCounter)
        return repCounter

kaprekasConstant(userInput, repCounter)