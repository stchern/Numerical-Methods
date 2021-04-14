from file_read_backwards import FileReadBackwards


def f(x):
    #return 0
   return 2*x + 3

def p(x):
    return 1

def q(x):
    return -2

def u(x, z, y):
    return f(x) + q(x)*y 

def v(x, z, y):
    return z

def func_1(x ,y1, y2):
    return q(x) - (y1**2)/p(x)

def func_2(x, y1, y2):
    return f(x) - (y1*y2)/p(x)

def func_12(x,y1,y2):
    return 1/(p(x)) - q(x)*y1**2

def func_22(x,y1,y2):
    return f(x)*y1 - q(x)*y1*y2


def integrator_3 (x, y1, y2, h, func_1 = func_1, func_2 = func_2):
    
    a = 1/3
    k1_1 = h * func_1( x, y1, y2)
    k1_2 = h * func_2( x, y1, y2)
    k2_1 = h * func_1( (x + a * h), ( y1 + a*k1_1), ( y2 + a*k1_2))
    k2_2 = h * func_2( (x + a * h), ( y1 + a*k1_1), ( y2 + a*k1_2))
    k3_1 = h * func_1( (x + 2 * a * h), (y1 + 2 * a * k2_1), (y2 + 2 * a * k2_2))
    k3_2 = h * func_2( (x + 2 * a * h), (y1 + 2 * a * k2_1), (y2 + 2 * a * k2_2))
    
    y1 = y1 + 1/4 * ( k1_1 + 3 * k3_1)
    y2 = y2 + 1/4 * ( k1_2 + 3 * k3_2)
    return y1, y2

def step1(a, b, a3_c, b3_c,func_1,func_2, filename):

    print("step1")
    infile = open(filename,"rt")
    h = -0.1
    a3i, b3i = integrator_3(b, a3_c, b3_c, h)
             
    with FileReadBackwards(filename) as frb:
        line_i = [float(i) for i in frb.readline().split(' ')]
        i,xi = line_i[0], line_i[1]
            
        for line in frb:
            print("i:",i," xi: ",xi, " a3i: ", round(a3i,5), " b3i: ", round(b3i,5))
            line_i = [float(i) for i in line.split(' ')]
            i,xi = line_i[0], line_i[1]
            if (xi == a):
                break
    
            a3i,b3i = integrator_3(xi, a3i, b3i,h, func_1,func_2)


            
    infile.close()
    return a3i, b3i

def step2(a, b, z_a, y_a, infile, outfile):

    print("step2")
    infile = open(infile,"rt")
    outfile = open(outfile, "w")

    for _ in range(2):
        line = infile.readline()
    
    line = infile.readline()
    line_i = [float(i) for i in line.split(' ')]
    i,xi = line_i[0], line_i[1]
        
    h = 0.1
    zi, yi = integrator_3(a, z_a, y_a, h, u, v)
    
    for line in infile:
        line_i = [float(i) for i in line.split(' ')]
        i,xi = line_i[0], line_i[1]
        writeOutput(outfile, int(i), xi, yi, zi)
       # print("i:",i," xi: ",xi, " zi: ", round(zi,5), " yi: ", round(yi,5))
       
        zi,yi = integrator_3(xi, zi, yi, h, u, v)
        if (xi+h >= b):
            break
    
    writeOutput(outfile, int(i+1), xi+h, yi, zi)
    infile.close()
    outfile.close()
    return zi, yi


def writeOutput(outfile,i, xi, yi, zi):
    s = ": x[" + str(i) + "]= " + str(round(xi,6))
    s += "  y[" + str(i) + "]= " + str(round(yi,6))
    s += "  y'[" + str(i) + "]= " + str(round(zi,6)) + '\n'
    outfile.write(s)

def testIput(filename):
    infile = open(filename,"rt")

    line = infile.readline()
    line = [float(i) for i in line.split(' ')]
    a1, b1, g1, a2, b2, g2 = line[0], line[1], line[2], line[3],line[4], line[5]
    line = infile.readline()
    line = [float(i) for i in line.split(' ')]
    a, b, count = line[0], line[1], line[2]
    print("a1: ",a1," b1: ",b1," g1: ",g1)
    print("a2: ",a2," b2: ",b2," g2: ",g2)
    print("a: ",a," b: ",b," count: ",count)
    
    icod = 0
    if ((a >= b) or (count < 0)): 
        icod = 3
    
    infile.close()
    
    return a1, b1, g1, a2, b2, g2, a, b, count, icod


def main():
    infile = "input1.txt"
    outfile = "output1.txt"
    a1, b1, g1, a2, b2, g2, a, b, count, icod = testIput(infile)
    
    if ( icod == 3 ):
        print ("input error\n")
        return icod

    c = b
    if (a2 != 0):
        a3_c = (-b2 * p(c)) / a2
        b3_c = ( g2 * p(c)) / a2
        print("a3_c:", a3_c, " b3_c: ", b3_c)
        a3, b3 = step1(a, b, a3_c, b3_c,func_1, func_2, infile)
        print("a3,b3: ", a3, " ", b3)
        g3 = b3
        b3 = -a3
        a3 = p(a)

    else:
        if ( b2 != 0):
            phi_c = (-a2) / (b2*p(c))
            psi_c = -g2 / b2
            phi, psi = step1(a, b, phi_c, psi_c,func_12, func_22, infile)
            g3 = psi
            b3 = -1
            a3 = phi*p(a)


    det = a3*b1 - a1*b3
    if (det == 0):
        icod = 2
        return icod
    if ( (a3 == a1) and (b3 == b1) and (g3 == g1)):
        icod = 1
        return icod

    print("DET:", det)
    z_a = (g3*b1 - g1*b3) / det
    y_a = (a3*g1 - a1*g3 ) / det

    print("dya: ", z_a, "y_a:", y_a)
    z, y = step2(a, b, z_a, y_a, infile,outfile)

    print("dy: ", z, "y:", y)


if __name__ == "__main__":
    main()

