a=float(input('Nhap a='))
b=float(input('Nhap b='))
c=float(input('Nhap c='))
if a>b and a>c:
    max=a 
elif b>a and b>c:
    max=b
else: 
    max=c
if a<b and a<c:
    min=a
elif b<a and a<c:
    min=b
else:
    min=c
print('SLN=',max,sep='')
print('SBN=',min,sep='')