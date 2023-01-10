# Assumptions:
# 1. String characters are not specifically ASCII
# 2. A substring of a string is a valid permutation

# Time complexity: O(a + b)
#   - 2 for loops that iterate over 2 distinct strings without nesting
# Space complexity: O(N)
#   = creating and maintaining a dictionary takes N spaces

def dictBuilder(str):
    dct = {}
    for i in range(len(str)):
        if str[i] in dct.keys():
            dct[str[i]] += 1
        else:
            dct[str[i]] = 1
    
    return dct

def checkPermutation(str1, str2):
    counterDict = {}
    smallerStr = ""

    if len(str1) < 1 or len(str2) < 1:
        return False

    if len(str1) >= len(str2):
        smallerStr = str2
        counterDict = dictBuilder(str1)
    else:
        smallerStr = str1
        counterDict = dictBuilder(str2)

    for i in range(len(smallerStr)):
        if (smallerStr[i] not in counterDict.keys()) or (counterDict[smallerStr[i]] == 0):
            return False
        else:
            counterDict[smallerStr[i]] -= 1
    
    return True


print("Passing test results for checkPermutation()")
print(checkPermutation("", ""))
print(checkPermutation("abcdef", "abc"))
print(checkPermutation("abc", "abcdef"))
print(checkPermutation("abcdef", "abcg"))
print(checkPermutation("abcdef", ""))
print(checkPermutation("a", "b"))
print(checkPermutation("a", "a"))