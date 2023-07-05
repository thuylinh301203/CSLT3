a=float(input('x='))
b=float(input('y='))
c=input('Phep toan:')
if c=="+" or c=="-" or c=='*' or c=='/':
    if c=='+':
        print(str(a),'+',str(b),'=',round(a+b,1),sep='')
    elif c=='-':
        print(str(a),'-',str(b),'=',round(a-b,1),sep='')
    elif c=='*':
        print(str(a),'*',str(b),'=',round(a*b,1),sep='')
    elif c=='/':
        if b==0:
            print('Khong hop le')
        else:
            print(str(a),'/',str(b),'=',round(a/b,1),sep='')
else:
    print('Khong hop le')