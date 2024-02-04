
def min_heap(a,i):
    l=2*i+1
    r=2*i+2
    if l<len(a) and a[l]<a[i]:
        s=l
    else:
        s=i
    if r<len(a) and a[r]<a[s]:
        s=r
    if s!=i:
        a[i],a[s]=a[s],a[i]
        min_heap(a,s)
def hape(a):
    n=len(a)//2 -1
    for i in range(n,-1,-1):
        min_heap(a,i)

a=[3,9,2,1,4,5]
hape(a)
print(a)