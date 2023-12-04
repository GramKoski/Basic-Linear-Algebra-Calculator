L = [[1, 2, 3],[4, 5, 6],[7, 8 ,9]]
A1 = [[5,6], [7, 8]]
A2 = [[6,1,1],[4, -2, 5],[2,8,7]]
import functools

def addition(X,Y):
	return [[X[row][column] + Y[row][column] for column in range(len(X[0]))] for row in range(len(X))]
	
def subtraction(X,Y):
	return [[X[row][column] - Y[row][column] for column in range(len(X[0]))] for row in range(len(X))]

def multiply(X, Y):
	if len(X[0]) != len(Y):
		return 'matrices are not multipliable'
	else:
		return [[sum([a[i]*b[i] for i in range(len(a))]) for a in transpose(Y)] for b in X]
		
def transpose(X):
	return [[X[column][row] for column in range(len(X[0]))] for row in range(len(X))]

def subMatrix(M,i,j):
	return [[M[row][column] for column in range(len(M)) if column != j] for row in range(len(M)) if row != i]
	
def minor(M, i, j):
	return det(subMatrix(M, i, j))

def cofactor(M,i,j):
	return (-1)**((i+1)+(j+1))*minor(M, i, j)

def det(M):
	if len(M) == 1:
		return M[0][0]
	else:
		return sum([cofactor(M, 0, j) * M[0][j] for j in range(len(M))])
#for i in range (len(M))])

def coMatrix(M):
	return [[cofactor(M, i, j) for j in range(len(M))] for i in range(len(M))]