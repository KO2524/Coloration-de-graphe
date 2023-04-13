# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:06:29 2023

@author: Karl Olivet
"""
n=10     #nombre de noeuds
L=[[0,1],[0,3],[1,2],[1,4],[2,3],[3,6],[4,5],[4,7],[5,6],[5,8],[6,9],[7,8],[7,9],[8,9]] #Liaison entre chaque noeuds
#algorithme de création du graphe
def graphe(n,L):
    E=[[0 for y in range(n-i-1)] for i in range(n)]
    for i in L:
        E[i[0]][i[1]-i[0]-1]=1
    return E

E=graphe(10,L)
print(E)


def nb_chromatique(n,E,w=1):
    F=[]
    V=list(range(n))
    v=n
    while v>0:
        M=[]
        m=0
        k=0
        DM=[]
        for a in V[1:]:
            if E[V[0]][a-V[0]-1]==0:
                M.append(a)
                m+=1
        a=0
        for A in M[:m-1]:

            b=0
            for B in M[a+1:]:
                if E[A][B-A-1]==1:
                    DM.append([a,b])
                    k+=1
                b+=1
            a+=1
        if k!=0:
            M_=nb_chromatique(m, [[1 if [i,j] in DM else 0 for j in range(m-i-1)] for i in range(m)],0)[0][0]
            M=[M[i] for i in M_]
            m=len(M_)
        v-=m+1
        F.append([V[0]]+M)
        v=w*v
        print("F",v)
        if v==0:
            return F,len(F)
        else:
            V=[x for x in V if x not in [V[0]] + M]

            

        
print(nb_chromatique(n,E))       