import mainFunction as mf

def test(n,lambdaRange,epsilonAcc,M):
    lambdaAccuracy = 0
    xAccuracy = 0
    R = 0
    lambdaVect = mf.generateLambda(n,lambdaRange)
    diagonalM = mf.DiagonalMatrix(lambdaVect,n)
    housholderM = mf.HousholderMatrix(n,m)
    A = mf.mult(mf.mult(housholderM,diagonalM),housholderM.transpose())

    epsilonL = mf.generateError(epsilonAcc)
    epsilonX = mf.generateError(epsilonAcc)
    lambdaN = lambdaVect[n-1]+epsilonL
    lambdaN1 = lambdaVect[n-2]+epsilonL
    lambdaN2 = lambdaVect[n-3]
    xn = mf.np.array(housholderM[:][n-1]).reshape(n,1)
    xn1 = mf.np.array(housholderM[:][n-2]).reshape(n,1)
    xn2 = mf.np.array(housholderM[:][n-3]).reshape(n,1)
    x_n = mf.np.array([x+epsilonX for x in xn]).reshape(n,1)
    x_n1 = mf.np.array([x+epsilonX for x in xn1]).reshape(n,1)
    for _ in range(10):
        x_n2, lambda_N2, k, r = mf.mainAlgorithm(n, A, lambdaN, lambdaN1, x_n, x_n1, epsilonL, epsilonX, M)
        lambdaAccuracy += abs(lambda_N2 - lambdaN2)
        xAccuracy += abs((mf.scalarProduct(x_n2,xn2))/(mf.norm(x_n2)*mf.norm(xn2)))
        R += r
    print ('mean Lambda Accuracy:', "%.3g"%(lambdaAccuracy/10),'\n')
    print ('mean X Accuracy:', "%.3g"%(xAccuracy/10),'\n')
    print ('R Accuracy:', "%.3g"%(R/10),'\n') 

def testN(size):
    n = size
    lambdaRange = 2
    epsilonAcc = 10**(-3)
    M = 50
    test(n,lambdaRange,epsilonAcc,M)
    M = 100
    test(n,lambdaRange,epsilonAcc,M)

    epsilonAcc = 10**(-6)
    M = 50    
    test(n,lambdaRange,epsilonAcc,M)
    M =100        
    test(n,lambdaRange,epsilonAcc,M)

    lambdaRange = 50
    epsilonAcc = 10**(-3)
    M = 50
    test(n,lambdaRange,epsilonAcc,M)
    M = 100
    test(n,lambdaRange,epsilonAcc,M)

    epsilonAcc = 10**(-6)
    M = 50    
    test(n,lambdaRange,epsilonAcc,M)
    M =100        
    test(n,lambdaRange,epsilonAcc,M)
    

n=3
m=4
#     create matrix A
lambdaVect=mf.generateLambda(n,m)
diagonalM=mf.DiagonalMatrix(lambdaVect,n)
housholderM=mf.HousholderMatrix(n,m)
A = mf.mult(mf.mult(housholderM,diagonalM),housholderM.transpose())

#print('lambda: ', lambdaVect,'\n')
#print('diagonal matrix: ', diagonalM,'\n')
#print('householder:',housholderM,'\n')
#print('A:',A, '\n')

#    create eigenvalue and eigenvector 
epsilonL = mf.generateError(10**(-6))
epsilonX = mf.generateError(10**(-6))
lambdaN = lambdaVect[n-1]+epsilonL
lambdaN1 = lambdaVect[n-2]+epsilonL
xn=mf.np.array(housholderM[:][n-1]).reshape(n,1)
xn1=mf.np.array(housholderM[:][n-2]).reshape(n,1)
x_n = mf.np.array([x+epsilonX for x in xn]).reshape(n,1)
x_n1 = mf.np.array([x+epsilonX for x in xn1]).reshape(n,1)

#print('epsilon: ',epsilonL,'\n')
#print(lambdaN,' ',lambdaN1,'\n')
#print('xn:',x,'\n')
#print('Ax:', mf.mult(A,x),'\n')
#print(mf.np.array(x)*lambdaVect[n-1],'\n')
#print('x_n: ',x_n,'\n','x_n1: ',x_n1,'\n')
x_n2, lambdaN2, k, r = mf.mainAlgorithm(n, A, lambdaN, lambdaN1, x_n, x_n1, epsilonL, epsilonX, 1000)
print('l: ',lambdaN2,'\n\n ','x: ',x_n2,' \n\n','k: ',k,'\n ','r: ',r)



