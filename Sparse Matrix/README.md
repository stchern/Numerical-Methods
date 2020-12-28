Solving Linear Systems with sparse matrix

b- main diagonal vector
a- lower codiagonal vector
c - upper codiagonal vector
q - vector of the k-th row of matrix
p - vector of the l-th row of matrix
f - vector of the right side of system equations

Matrix:

![](matrix.png/150x100)
b0  c0  0  0  0 ... 0 0
a1  b1  c1 0  0 ... 0 0
0   a2  b2 c2 0 ... 0 0
...
0   0   0  0  0 ...c[n-2] 0    
q0  q1  q2 q3 q4...q[n-2] q[n-1]
p0  p1  p2 p3 p4...q[n-2] p[n-1] 

in addition:
 a[0]=c[n-1]=0
 p[n-3]=a[n-2]
 p[n-2]=b[n-2]
 p[n-1]=c[n-2]
 q[n-2]=a[n-1]
 q[n-1]=b[n-1]