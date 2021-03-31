import numpy as np 

def generateVector(n,m):
    return np.array([(-1)**np.random.randint(3)*(m*np.random.random()-m) for i in range(n)])

def generateError(epsilon):
    return (-1)**np.random.randint(3)*(epsilon*np.random.random()-epsilon)

def generateLambda(n,m):
    vector = np.array([(-1)**np.random.randint(3)*(m*np.random.random()-m) for i in range(n)]) 
    return sorted(vector, key=abs)

def firstNorm(v):
    return max([abs(x) for x in v]) 

def norm(v):
    length = sum([x*x for x in v])
    length = length**(1/2)
    return length

def normalizedVector(v):
    n = v.shape[0]
    length = norm(v)
    vector = np.array([x/length for x in v]).reshape(n,1)
    return vector 

def scalarProduct(v1,v2):
    n = v1.shape[0]
    scalar = 0
    for i in range(n):
        scalar += v1[i][0]*v2[i][0]
    return scalar

def mult(matrix1,matrix2):
    n1 = matrix1.shape[0]   
    m1 = matrix1.shape[1]
    n2 = matrix2.shape[0]
    m2 = matrix2.shape[1]

    matrix = np.zeros((n1,m2))
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return matrix

def subtract(matrix1, matrix2):
    n = matrix1.shape[1]
    if(n > 1):
        matrix = np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix1[i][j]-matrix2[i][j]
    else:
        matrix = np.zeros((n,1))
        for i in range(n):
            matrix[i][0] = matrix1[0][i]-matrix2[0][i]
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

def DiagonalMatrix(lambdaArr, n):
    matrix = np.zeros((n,n))
    for i in range(n):
        matrix[i][i] = lambdaArr[i]
    return matrix

def HousholderMatrix(n,m):
    matrix = np.identity(n)
    w = generateVector(n,m)
    w = normalizedVector(w)
    v = mult(w,w.transpose())
    matrix = subtract(matrix, 2*v)
    return matrix


def mainAlgorithm(n, A, lambdaN, lambdaN1, x_n, x_n1, epsilonL, epsilonX, M):
    A1 = subtract (subtract(A, lambdaN * mult( x_n, x_n.transpose() )),
                                lambdaN1 * mult(x_n1, x_n1.transpose() ))
    v_k = v_prev = x_k = x_n1
    gamma_k = gamma_prev = lambdaN1
    e_l1 = epsilonL
    e_x1 = epsilonX
    K = 0 

    while( (K<M) & (e_l1 >= epsilonL) & (e_x1 >= epsilonX) ):
        v_k = normalizedVector(x_k)
        x_k = mult(A1,v_k)
        gamma_k = mult(v_k.transpose(),x_k)
        K+=1

        e_l1 = abs(gamma_prev - gamma_k)
        e_x1 = abs((scalarProduct(v_prev,v_k))/(norm(v_prev)*norm(v_k)))

        v_prev = v_k
        gamma_prev = gamma_k
    
    r = firstNorm(subtract(mult(A,v_k),gamma_k*v_k))
    return v_k, gamma_k, K, r














