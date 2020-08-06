def printlist2d(m):
	for lst in m:
		for x in lst:
			print(x, end='\t')
		print()		    
    

n = int(input())
M = [[0] * n for i in range(n)]
for i in range(n):
	for j in range(n):
		if i + j == n - 1:
			M[i][j] = 1
		if i + j > n - 1:
			M[i][j] = 2
printlist2d(M)
