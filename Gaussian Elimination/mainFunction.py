import numpy as np 

def generateVector(n,m):
    return np.array([(-1)**np.random.randint(3)*(m*np.random.random()-m) for i in range(n)])

def mult(matrix1,matrix2):
    n1 = matrix1.shape[0]   
    m1 = matrix1.shape[1]
    m2 = matrix2.shape[1]

    matrix = np.zeros((n1,m2))
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return matrix

def createMatrix(n,m):
    matrix = np.ones((n,n))
    for i in range(n):
        matrix[i] = generateVector(n,m)
    return matrix

def HilbertMatrix(n):
    matrix=np.ones((n,n))
    for i in range(n):
        for j in range(n):
            matrix[i][j]=1/(i+j+1)
    return matrix

def accuracy(x,x_true,n):
    max=0
    q=n*2/3
    for i in range(n):
       dif=abs(x[i]-x_true[i])
       dif2=dif/abs(x_true[i])
       if abs(x_true[i])>q :
           if max<dif2:
              max=dif2
       else:
           if max<dif:
              max=dif
    return max


def mainAlgorithm(matrix,f):
    n=matrix.shape[0]
    matrix=np.column_stack((matrix,f))

    for i in range (n):
        R=1/matrix[i][i]
        matrix[i][i]=1

        for j in range(i+1,n+1):
            matrix[i][j]*=R

        for k in range(i+1,n):
            R=matrix[k][i]
            matrix[k][i]=0

            for j in range(i+1,n+1):
                matrix[k][j]-=R*matrix[i][j]
                

    x=np.zeros(n)
    for i in range(n-1,-1,-1):
        s=matrix[i][n]

        for k in range(i+1,n):
            s-=matrix[i][k]*x[k]

        x[i]=s/matrix[i][i]

    return x




