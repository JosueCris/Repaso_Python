import math
import random
def le(men):
     print(men)
def ci(men):
    vi=int(input(menn))
    return vi
def cf(men):
    vi=float(input(men))
    return vi
def lf(men,var):
     print(men,var)
def lfs(men,var):
     print(men,var,end='')
def lffs(men,var):
    print(men,end='')
    print("{:3.2f} ".format(var),end='\n')
def lff(men,var):
     print(men,end='')
     print(":{3.2f} ".format(var),end='')
def capv(v,n):
     s=0;menor=100000;mayor=0
     for x in range(1,n+1):
          b=cf("dame el dato: ")
          v.append(b)
          s=s+v[x]
     return s
def bur(v,n):
    for x in range(1,n):
         for y in range(x+1,n+1):
              if(v[x]>v[y]):
                   t=v[x]
                   v[x]=v[y]
                   v[y]=t
def impv(v,n):
    for x in range(1,n+1):
         lf("valor: ",v[x])
def med(v,n):
     if(n%2==1):
          lf("la mediana es: ",v[int((n+1)/2)])
     else:
         p=(v[int(n/2)]+v[int(n/2)+1])/2
         lf("la mediana es: ",p)
def meds(v,n):
     if(n%2==1):
          p=v[int((n+1)/2)]
     else:
          p=(v[int(n/2)]+v[int(n/2)+1])/2
     return p
def moda(v,n):
    t=1;x=1
    while x < n:
        for y in range(x+1,n+1):
            if(v[x]==v[y]):
                t=t+1
            else:
                y=n+1
            if(t>1):
                print (v[x],":",t)
                x=x+t;t+1
            else:
                x=x+1
def vari(v,n,s):
        sv=sv/(n-1)
        return sv
def impesta(v,n,s):
    bur(v,n);
    lf("El menor es: ",v[1])
    lf("El mayor es: ",v[n])
    lf("La media es: ",s/n)
    lf("La mediana es: ",meds(v,n))
    lf("La varianza es: ",vari(v,n,s))
    lf("La desv. estandar es: ",math.sqrt(vari(v,n,s)))
    moda(v,n)
def impestas(v,n,s):
    bur(v,n);
    lff(" ",v[1])
    lff(" ",v[n])
    lff(" ",s/n)
    lff(" ",meds(v,n))
    lff(" ",vari(v,n.s))
    lffs(" ",math.sqrt(vari(v,n,s)))
    moda(v,n)
def vvai(v,n,vi,vf):
    s=0
    for x in range(1,n+1):
        b = random.randint(vi, vf)
        v.append(b)
        s=s+b
    return s
def cap_mat(m1,nf,nc):
    for f in range(nf):
        m1.append([])
        for c in range(nc):
          valor=cv("valor: ")
          m1[f].append(valor)
def imp_mat(m1,nf,nc):
    for f in range(nf):
        for c in range(nc):
            print (m1[f][c],end=" ")
        print()
def imp_matf(m1):
    for f in m1:
        print("[", end=" ")
        for c in f:
            print("{:3.2f}".format(c),end=" ")
        print("]")
    print()
def suma2_m(m3,m1,m2,nf,nc):
    for f in range(nf):
        m3.append([])
        for c in range(nc):
            m3[f].append(m1[f][c]+m2[f][c])
def mult2_m(m3,m1,m2):
    for f in range(len(m1)):
       m3.append([])
       for c in range(len(m2[0])):
            for u in range(len(m1[0])):
                m3[f][c]+=(m1[f][u]*m2[u][c])

    

    
        
