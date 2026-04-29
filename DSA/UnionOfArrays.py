def UnionArray(l,r):
    res=[]
    i,j=0,0
    m,n=len(l),len(r)

    while i<m and j<n:
        if l[i]<=r[j]:
            if len(res)==0 or res[-1]!=l[i]:
                res.append(l[i])
            i+=1
        else:
            if len(res)==0 or res[-1]!=r[j]:
                res.append(r[j])
            j+=1
    
    while i<m:
        if len(res)==0 or res[-1]!=l[i]:
            res.append(l[i])
        i+=1
    
    while j<n:
        if len(res)==0 or res[-1]!=r[j]:
                res.append(r[j])
        j+=1
        
    return res

a=[1,2,2,3,4,6,8]
b=[2,3,3,4,5,5,6]

print(UnionArray(a,b))