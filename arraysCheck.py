A = [1, 2, 5, 4, 0]
B = [2, 4, 5, 0, 1]

C = [1, 1, 0, 0]
D = [1, 1, 0, 0, 0]

def arrayChk(arr1, arr2):
    print(arr1)
    print(arr2)
    if len(arr1) == len(arr2):
        arr1.sort()
        arr2.sort()
        if (arr1 == arr2):
            print("The given arrays are equal")
            return None
    print("The given arrays are not equal")

arrayChk(A, B)
arrayChk(C, D)