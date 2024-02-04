def maxheap(a,k):
    l=2*k +1
    r=2*k +2
    if l<len(a) and a[l]>a[k]:
        lar=l
    else:
        lar=k
    if r<len(a) and a[r]>a[lar]:
        lar=r
    if lar!=k:
        a[k],a[lar]=a[lar],a[k]
        maxheap(a,lar)
def maxh(a):
    n=len(a)//2 -1
    for i in range(n,-1,-1):
        maxheap(a,i)


a=[3,9,2,1,4,5]
maxh(a)
print(a)