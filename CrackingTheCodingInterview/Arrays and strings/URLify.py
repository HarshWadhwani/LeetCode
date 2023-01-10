# Pythonic solution

# Time complexity: O(N)
#   - strip() and replace() take O(N) time 
# Space complexity: O(1)
#   = no additional space required

def uRLifyPythonic(str):

    return str.strip().replace(" ", "%20")

print("Passing test results for uRLify()")
print(uRLifyPythonic("My Name Is  Harsh      "))

def uRLify(str, trueLengthOfStr):
    for i in range()