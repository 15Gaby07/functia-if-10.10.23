#- problema 6
a=int(input('a= '))
b=int(input('b= '))
if (a-1==b) or (b-1==a):
    print('DA')
else:
    print('NU')

#- problema 5
a=int(input('a= '))
b=int(input('b= '))
if a>b:
    print(a*2, b*3)
elif b>a:
    print(b*2, a*3)
else:
    print('nr sunt egale')

#- problema 4
a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
s=int(input('suma adoua nr extrase= '))
st= a+b+c
if st-s==a:
    print('a ramas nr. = ', a)
elif st-s==b:
    print('a ramas nr. = ', b)
else:
    print('nu ai introdus corect')

#- problema 3
p1=int(input('punctaj primul sportiv=  '))
p2=int(input('punctaj al doilea sportiv=  '))
if p1>p2:
    print(p1,p2)
else:
    print(p2,p1)

#- problema 2
a=int(input('vasrta copil1=  '))
b=int(input('varsta copil2=  '))
if a>b:
    print('primul copil e mai mare cu  ',a-b,'ani')
elif b>a:
    print('al 2 copil e mai mare cu  ',b-a,'ani')
else:
    print('copii au aceeasi varsta')

#- problema 1
a=int(input('a= '))
b=int(input('b= '))
if a>b:
    print('cel mai mic este=  ',b)
elif b>a:
    print('cel mai mic este= ', a)   
else:
    print('nr sunt egale')    

