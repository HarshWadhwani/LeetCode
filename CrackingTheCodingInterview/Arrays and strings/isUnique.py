#Time complexity: O(n^2)
#   - nested for loops

def isUnique(str):

    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if str[i] == str[j]:
                return False
    
    return True

print("Passing test results for isUnique()")
print(isUnique(""))
print(isUnique("a"))
print(isUnique("abc"))
print(isUnique("abcc"))
print(isUnique("aaaaa"))

#Time complexity: O(n)
#   - iterates through length of string once. n = length of string
#Space complexity: O(1)
#   - length of countList is fixed (Assuming ASCII encoding)


def isUniqueWithCounter(str):

    if len(str) > 128:
        return False

    countList = [0] * 128

    for i in range(len(str)):
        if countList[ord(str[i])] == 0:
            countList[ord(str[i])] += 1
        else:
            return False
    
    return True

print("Passing test results for isUniqueWithCounter()")
print(isUniqueWithCounter(""))
print(isUniqueWithCounter("a"))
print(isUniqueWithCounter("abc"))
print(isUniqueWithCounter("abcc"))
print(isUniqueWithCounter("aaaaa"))


