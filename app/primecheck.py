from math import sqrt,floor;
def prime(num):
    #N=floor(sqrt(num))
    if(num<2):
        return False
    elif (num==2):
        return True
    else:
        for i in range(2,floor(sqrt(num)),1):
            if(num%i==0):
                return False
        return True