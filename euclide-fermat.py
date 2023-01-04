#this method uses the Euclide algorithm
# two numbers a,b are coprime if their GCD is 1
def GCD(a,b):
    if(b>a):
        c=a
        a=b
        b=c
    if(a%b==0):
        return b
    div=a//b
    r=a-(div*b)
    rr=r
    while(r!=0):
        a=b
        b=r
        div=a//b
        r=a-(div*b)
        if(r==0):
            return rr
        rr=r
    return rr+1

def GCDQ(a,b):
    quots=[]
    if(b>a):
        c=a
        a=b
        b=c
    if(a%b==0):
        return b
    div=a//b
    r=a-(div*b)
    quots.append(div)
    while(r!=0):
        a=b
        b=r
        div=a//b
        r=a-(div*b)
        quots.append(div)
        if(r==0):
            return quots
    return quots

def isprime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def extendedEuclides(a,b):
    if(GCD(a,b)!=1):
        print("a and b are not coprimes!")
        return None
    quots=GCDQ(a,b)
    x=[1,0]
    y=[0,1]
    for j in range(2,len(quots)+1):
        x.append((quots[j-2]*-1)*x[j-1]+x[j-2])
        y.append((quots[j-2]*-1)*y[j-1]+y[j-2])
        finx=x[j]
        finy=y[j]

    return [finx,finy]

#the totient phi function allow us to obtain the exact number of numbers that are coprime with n!
def totient_phi(n):
    if(isprime(n)==True):
        return (n-1)
    divs=[]
    for i in range (2,n):
        if(isprime(i) and n%i==0):
            divs.append(i)

    tot=1
    for i in divs:
        tot=tot*(1-1/i)

    tot*=n
    return tot

def totient_phi_fact(p,q):
    if(isprime(p) and isprime(q)):
        return(p-1)*(q-1)
    else:
        print("p and q are not prime numbers!")

def menu():
    print("[1] to calculate GCD of 2 numbers")
    print("[2] to calculate the multiplicative inverse of 2 coprime numbers")
    print("[3] to calculate the totient function phi of a number n")
    print("[0] to quit")
    choice=int(input())
    return choice

def main():
    choice=1
    while(choice!=0):
        choice=menu()
        if(choice==1):
            a=int(input("Input number a: "))
            b=int(input("Input number b: "))
            gcd=GCD(a,b)
            print("GCD is: "+str(gcd))
        elif(choice==2):
            a=int(input("Enter first number a: "))
            b=int(input("Enter second number b: "))
            euc=extendedEuclides(a,b)
            if(euc==None):
                continue
            gcd=GCD(a,b)
            print("Your GCD is: "+str(gcd))
            print("Considering the form a*x + b*y EQUIV 1 mod "+str(gcd))
            print("your x is : "+str(euc[0]))
            print("your y is : "+str(euc[1]))
        elif(choice==3):
            a=int(input("Enter the number which you want to calculate PHI of: "))
            tot=totient_phi(a)
            print(tot)

main()
