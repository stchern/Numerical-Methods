import math

def mach_eps():
    r = 1
    while ((1 + r) > 1):
        r = r/2
    return r*2

macheps = mach_eps()

def func(x, y):
    return x**2 - 2*y
    #return -y
    #return 45*x**4

def eps_loc(y3,y4):
   return y4 - y3

def new_h(eps_l, h, eps):

    uncorrected_x = False
    eps_l = abs(eps_l)

    if ( not eps_l ):
        eps_l = eps_l + macheps
    if ( eps_l >= eps ):
        uncorrected_x = True

    alpha = (eps / eps_l)**(1/4)
    alpha = 0.9 * alpha

    h = alpha*h
    while ( h < macheps ):
        h += macheps

    return h, uncorrected_x


def integrator_3 (x, y, h):
    a = 1/3
    k1 = h * func( x, y)
    k2 = h* func( (x + a * h), ( y + a*k1))
    k3 = h * func( (x + 2 * a * h), (y + 2 * a * k2))
    y = y + 1/4 * ( k1 + 3 * k3)
    return y


def integrator_4 (x, y, h):
    a = 1/3
    k1 = h * func( x, y)
    k2 = h* func( (x + a * h), ( y + a*k1))
    k3 = h * func( (x + 2 * a * h), (y - a * k1 + k2))
    k4 = h * func( (x + h), (y - k1 - k2 + k3))
    y = y + 1/8 * ( k1 + 3 * k2 + 3 * k3 + k4 )
    return y

def testIput(filename):
    infile = open(filename,"rt")

    string = infile.readline()
    string = [int(i) for i in string.split(' ')]
    a, b, c, y_c = string[0], string[1], string[2], string[3]
    string = infile.readline()
    string = [float(i) for i in string.split(' ')]
    h_min, h_max, eps = string[0], string[1], string[2]
    print("a: ",a," b: ",b," c: ",c, " yc:", y_c)
    print("hmin: ",h_min," hmax: ",h_max," eps: ",eps)
    
    icod = 0
    if ((a >= b) or ( ((c-a) * (c-b)) != 0) or  ( (h_min * h_max) < 0) or (eps < 0)): 
        icod = 2
    
    infile.close()
    
    return a, b, c, y_c, h_min, h_max, eps, icod

def writeOutput(outfile, q, i, xi, yi, eps_l):
    s = "q=" + str(q)+": x[" + str(i) + "]= " + str(round(xi,6))
    s += "  y[" + str(i) + "]= " + str(round(yi,6)) + '\n'
    if (q == 4):
        s+= " eps_loc: " + str(round(eps_l,6)) + '\n'
    outfile.write(s)
        


def main(filename):

    a,b,c,y_c,h_min, h_max, eps, icod = testIput(filename)
    min_step = 0
    max_step = 0
    uncorrected_x = 0
    
    if ( icod == 2 ):
        print ("input error\n")
        return icod

    outfile = open("output.txt", "w")

    writeOutput(outfile, 0, 0, a, y_c, 0)
    
    h = (b - a) / 10
    
    yi_3 = integrator_3(a, y_c, h)
    yi_4 = integrator_4(a, y_c, h)
    eps_l = eps_loc(yi_3,yi_4)
    i = 1
    xi = a + h
    writeOutput( outfile, 3, 1, xi, yi_3, eps_l)
    writeOutput( outfile, 4, 1, xi, yi_4, eps_l)

    h, un_x = new_h(eps_l, h, eps)

    if ( un_x ):
        uncorrected_x += 1

    if ( h <= h_min ):
        h = h_min
        min_step += 1
    elif ( h >= h_max ):
        h = h_max
        max_step += 1


    while ( xi + 2*h < b ):
        
        yi_3 = integrator_3( xi, yi_3, h)
        yi_4 = integrator_4( xi, yi_4, h)
        eps_l = eps_loc(yi_3,yi_4)
        i += 1
        xi += h
        writeOutput( outfile, 3, i, xi, yi_3, eps_l)
        writeOutput( outfile, 4, i, xi, yi_4, eps_l)

        h, un_x = new_h(eps_l, h, eps)

        if ( un_x ):
            uncorrected_x += 1

        if ( h <= h_min ):
            h = h_min
            min_step += 1
        elif ( h >= h_max ):
            h = h_max
            max_step += 1


    denom = 2
    while ( ((b - xi) / denom) >= h_max ):
        denom += 1

    h = (b - xi) / denom

    for _ in range(0,denom):
        
        yi_3 = integrator_3( xi, yi_3, h)
        yi_4 = integrator_4( xi, yi_4, h)
        eps_l = eps_loc(yi_3,yi_4)
        i += 1
        xi += h
        writeOutput( outfile, 3, i, xi, yi_3, eps_l)
        writeOutput( outfile, 4, i, xi, yi_4, eps_l)
        

    s = "\n count of x:" + str(i)+" uncorrected x: " + str(uncorrected_x)
    s +=" count of min step: " + str(min_step) + " count of max step: " + str(max_step) 
    outfile.write(s)
    
    outfile.close()


if __name__ == "__main__":
    main("input.txt")
