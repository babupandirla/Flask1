from math import sqrt,floor,log10;
def prime(num):
    #N=floor(sqrt(num))
    print(num)
    if(num<2):
        return False
    elif (num==2):
        return True
    else:
        #print(floor(sqrt(num)))
        for i in range(2,floor(sqrt(num))+1):
            #print(i)
            if(num%i==0):
                return False
        return True

def twosidedprime(num):
    if prime(num):
        leftcheck=True
        rightcheck=True
        temp=10
        while(num>temp):
            if prime(num%temp):
                temp=temp*10
            else:
                leftcheck=False
                break
        print('left done ' +str(leftcheck))
        digits = (int)(log10(num))  
        while(digits>0 and leftcheck):
            if prime((int)(num / pow(10, digits))):
                digits=digits-1
            else:
                rightcheck=False
                break
        return leftcheck and rightcheck
    else:
        return False    