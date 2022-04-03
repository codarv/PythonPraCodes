#Given an array of N integers. Find the first element that occurs K number of times. 
from operator import indexOf


N = 7
K = 2
A = [1, 7, 4, 3, 4, 8, 7]

def maxOccr(inList, K):
    candidates = {}
    for i in range(len(inList)):
        if inList[i] in candidates:
            candidates[inList[i]] = candidates.get(inList[i]) + 1
        else:
            candidates[inList[i]] = 1
        if candidates.get(inList[i]) == K:
            print("First element to occur " + str(K) + " times is: " + str(inList[i]))
            return None
    print(candidates)
maxOccr(A,K)