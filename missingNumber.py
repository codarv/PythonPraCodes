M = 5
A = [1, 2, 3, 5]

N = 10
B = [6, 1, 2, 8, 3, 4, 7, 10, 5]

def missingNumber(inList, S):
    chkList = [item for item in range(1,S+1)]
    if len(chkList) == len(inList):
        print("The given array has no missing element")
    else:
        diff = set(chkList).difference(inList)
    print(inList)
    print("The missing element is: " + str(diff) + "\n")

missingNumber(A, M)
missingNumber(B, N)