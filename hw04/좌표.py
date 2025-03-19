x=int(input('x 입력하기 : '))
y=int(input('y 입력하기 : '))

if x>0 and y>0:
    print('({}.{})는 1사분면 입니다.'.format(x,y))
elif x<0 and y>0:
    print('({}.{})는 2사분면 입니다. '.format(x,y))
elif x<0 and y<0:
    print('({}.{})는 3사분면 입니다. '.format(x,y))
elif x>0 and y<0:
    print('({}.{})는 4사분면 입니다. '.format(x,y))

