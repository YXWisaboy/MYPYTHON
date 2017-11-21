a=[1,3,2,5,8,4]

'''
for i in range(len(a)):
    for x in range(i+1,len(a)):
        if a[i]>a[x]:
            y=a[i]
            a[i]=a[x]
            a[x]=y
print(a)
'''

a=sorted(a)
print(a)
