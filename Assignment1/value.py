import math


sum = 0
term = 0
for m in range(0,5):
    term = pow(-1,m)/((2*m+1)*math.factorial(m))
    sum += term
    print("m:\t" + str(m) + "\tterm:\t" + str(term) + "\tsum\t" + str(sum))