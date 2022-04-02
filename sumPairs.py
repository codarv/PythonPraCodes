A = [1, 2, 4, 5, 7]
B = [5, 6, 3, 4, 8]
X = 9

C = [-1, -2, 4, -6, 5, 7]
D = [6, 3, 4, 0]
Y = 8
def sumPairs(InputA, InputB, X):
    res = []
    print("The pairs of sum equating to " + str(X) + " are:")
    for i in range(len(InputA)):
        for j in range(len(InputB)):
            if InputA[i] + InputB[j] == X:
                res.append(InputA[i])
                res.append(InputB[j])
                print(res)
        res.clear()

sumPairs(A,B,X)
sumPairs(C, D, Y)