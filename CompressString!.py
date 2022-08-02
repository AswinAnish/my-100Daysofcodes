from itertools import groupby
S=input()
for i,j in groupby(map(int,list(S))):
    print(tuple([len(list(j)), i]) ,end = " ")
