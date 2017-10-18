import numpy as np

L=3
J=1
S=np.random.choice([-1,1],(L,L))
print(S)

def h(s):
    E=0
    for i in range(L):
        for j in range(L):
            E=E-J*s[i,j]*(s[(i+1)%L,j]+s[i,(j+1)%L])
            
    return E

print(h(S))
