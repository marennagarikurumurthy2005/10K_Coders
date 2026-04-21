

def primecheck(sup):
    for i in range(2,sup):
        if sup%i==0:
            return False
    else:
        return True

n=1000
lf=n-1
rg=n+1
c=0
while True:
    if primecheck(lf)==0:
        lf-=1
    else:
        c+=1
    if primecheck(rg)==0:
        rg+=1
    else:
        c+=1
    if c==2:
        break
print(lf,n,rg)





