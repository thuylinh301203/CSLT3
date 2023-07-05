a=int(input('M1='))
b=int(input('M2='))
c=int(input('M3='))
d=int(input('S='))
if d<=100:
    print('Phai tra=',d*a,sep='')
elif 101<=d<=150:
    print('Phai tra=',100*a+(d-100)*b,sep='')
elif d>=151:
    print('Phai tra=',100*a+50*b+(d-150)*c,sep='')     