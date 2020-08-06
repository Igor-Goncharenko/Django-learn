def inputList2d(n): 
    return [[int(x) for x in input().split()] for i in range(n)]


def printList2d(m):
    for lst in m:
        for x in lst:
            print(x, end=" ")
        print()


n = int(input()) 
M = inputList2d(n)
flag = True
for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j] != M[j][i]:
            flag = False
if flag:
    print("yes")
else:
    print("no")
