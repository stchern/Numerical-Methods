
import numpy as np 
import mainFunction as mf

def test(n,m):
    meanSystemError=0
    meanAccuracy=0
    for _ in range(10):
        a=mf.generateVector(n,m)
        b=mf.generateVector(n,m)
        c=mf.generateVector(n,m)
        p=mf.generateVector(n,m)
        q=mf.generateVector(n,m)
        f=mf.generateVector(n,m)

        a[0]=c[n-1]=0
        p[n-3]=a[n-2]
        p[n-2]=b[n-2]
        p[n-1]=c[n-2]
        q[n-2]=a[n-1]
        q[n-1]=b[n-1]
         
        x=np.ones(n)
        x1=mf.generateVector(n,m)
        f=mf.multiplication(n,a,b,c,p,q,x)
        f1=mf.multiplication(n,a,b,c,p,q,x1)

        countOfTest=n
        try:
            x_f,x_f1=mf.mainAlgorithm(n,a,b,c,p,q,f,f1)
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)
            countOfTest-=1

        meanSystemError+=mf.mSystemError(x_f,n)
        meanAccuracy+=mf.mAccuracy(x1,x_f1,n)

    return (meanSystemError/countOfTest),(meanAccuracy/countOfTest)


n=10
m=10

meanSystemError,meanAccuracy=test(n,m)
print("%.3g"%meanSystemError," ","%.3g"%meanAccuracy)
        
a=mf.generateVector(n,m)
b=mf.generateVector(n,m)
c=mf.generateVector(n,m)
p=mf.generateVector(n,m)
q=mf.generateVector(n,m)
f=mf.generateVector(n,m)

a[0]=c[n-1]=0
p[n-3]=a[n-2]
p[n-2]=b[n-2]
p[n-1]=c[n-2]
q[n-2]=a[n-1]
q[n-1]=b[n-1]

x=np.ones(n)
x1=mf.generateVector(n,m)
f=mf.multiplication(n,a,b,c,p,q,x)
f1=mf.multiplication(n,a,b,c,p,q,x1)

try:
    x_f,x_f1=mf.mainAlgorithm(n,a,b,c,p,q,f,f1)
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

print("x: \n",x_f)
print("x1: \n",x_f1)
