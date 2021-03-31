
import numpy as np 
import mainFunction as mf

def testWellConditioned(n,m):
    meanAccuracy=0
    countOfTest=10
    for _ in range(10):
         
        matrix=mf.createMatrix(n,m)
        x=np.ones(n).reshape(n,1)
        f=mf.mult(matrix,x)         

        try:
            x_f=mf.mainAlgorithm(matrix,f)
            meanAccuracy+=mf.accuracy(x,x_f,n)
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)
            countOfTest-=1        

    return (meanAccuracy/countOfTest)

def testIllConditioned():
    for i in range(4,16,2):         
        matrix=mf.HilbertMatrix(i)
        x=np.ones(i).reshape(i,1)
        f=mf.mult(matrix,x)       

        try:
            x_f=mf.mainAlgorithm(matrix,f)
            print(i,": ","%.3g"%mf.accuracy(x,x_f,i),'\n')
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)

        
n=10
m=1

meanAccuracy=testWellConditioned(n,m)
print("%.3g"%meanAccuracy)
        
matrix=mf.createMatrix(n,m)
x=np.ones(n).reshape(n,1)
f=mf.mult(matrix,x)  
try:
    x_f=mf.mainAlgorithm(matrix,f)
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

print("x: \n",x_f)

testIllConditioned()
