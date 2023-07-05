a=int(input('Tieu thu='))
b=550
c=750
d=950
e=1350
if 1<=a<=100:
    print('Phai tra=',a*b+0.1,sep='')
elif 101<=a<=150:
    print('Phai tra=',100*b+(a-100)*c+0.1*(100*b+(a-100)*c),sep='')
elif 151<=a<=200:
    print('Phai tra=',100*b+50*c+(a-150)*d+0.1*(100*b+50*c+(a-150)*d),sep='')
elif a>=201:
    print('Phai tra=',100*b+50*d+50*c+(a-200)*e+0.1*(100*b+50*c+(a-200)*e),sep='')        