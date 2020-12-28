import numpy as np 

def generateVector(n,m):
    return np.array([(-1)**np.random.randint(3)*(m*np.random.random()-m) for i in range(n)])

def multiplication(n,a,b,c,p,q,x):
    f=np.zeros(n)
    f[0]=b[0]*x[0]+c[0]*x[1]
    for i in range (1,n-2):
        f[i]=a[i]*x[i-1]+b[i]*x[i]+c[i]*x[i+1]
    for i in range (n):
        f[n-2]+=p[i]*x[i]
        f[n-1]+=q[i]*x[i]
    return f

def createMatrix(n,m):
    matrix = np.ones((n,n))
    for i in range(n):
        matrix[i] = generateVector(n,m)
    return matrix

def mSystemError(x,n):
    return max([abs(x[i]-1) for i in range(n)])

def mAccuracy(x,x_true,n):
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


def mainAlgorithm(n,a,b,c,p,q,f,f1=0):
    k=n-2
    l=n-1
    for i in range (0,k-1):
        R=1/b[i]
        b[i]=1
        c[i]=R*c[i]
        f[i]=R*f[i]
        f1[i]=R*f1[i]
        R=a[i+1]
        a[i+1]=0
        b[i+1]=b[i+1]-R*c[i]
        f[i+1]=f[i+1]-R*f[i]
        f1[i+1]=f1[i+1]-R*f1[i]
        R=p[i]
        p[i]=0
        p[i+1]=p[i+1]-R*c[i]
        f[k]=f[k]-R*f[i]
        f1[k]=f1[k]-R*f1[i]
        R=q[i]
        q[i]=0
        q[i+1]=q[i+1]-R*c[i]
        f[l]=f[l]-R*f[i]
        f1[l]=f1[l]-R*f1[i]          
    R=1/b[k-1]
    b[k-1]=1
    c[k-1]=R*c[k-1]
    f[k-1]=R*f[k-1]
    f1[k-1]=R*f1[k-1]
    R=p[k-1]
    p[k-1]=a[k]=0
    b[k]=b[k]-R*c[k-1]
    p[k]=p[k]-R*c[k-1]
    f[k]=f[k]-R*f[k-1]
    f1[k]=f1[k]-R*f1[k-1]
    R=q[k-1]
    q[k-1]=0
    q[k]=q[k]-R*c[k-1]
    a[l]=a[l]-R*c[k-1]
    f[l]=f[l]-R*f[k-1]
    f1[l]=f1[l]-R*f1[k-1]

    R=1/b[k]
    b[k]=p[k]=1
    c[k]=R*c[k]
    p[l]=R*p[l]
    f[k]=R*f[k]
    f1[k]=R*f1[k]
    R=q[k]
    a[l]=q[k]=0
    b[l]=b[l]-R*p[l]
    q[l]=q[l]-R*p[l]
    f[l]=f[l]-R*f[k]
    f[l]=f[l]/q[l]        
    f1[l]=f1[l]-R*f1[k]
    f1[l]=f1[l]/q[l]
    b[l]=q[l]=1
    
    x=np.zeros(n)
    x1=np.zeros(n)
    x[l]=f[l]
    x1[l]=f1[l]
    for i in range(n-2,-1,-1):
        x[i]=f[i]-c[i]*x[i+1]
        x1[i]=f1[i]-c[i]*x1[i+1]
    return x,x1














