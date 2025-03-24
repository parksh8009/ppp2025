#왼쪽정렬 직각삼각형
n=int(input('삼각형의 높이를 입력하세요 : '))
for i in range(1,n+1):
    print('*'*i)

#오른쪽정렬 직각삼각형
m=int(input('삼각형의 높이를 입력하세요 : '))
for i in range(1,m+1):
    print(" "*(m-i)+ "*"*i)

#정삼각형
c=int(input('삼각형의 높이를 입력하세요 : '))
for i in range(1,c+1):
    print(' '*(c-i)+"*"*(2*i-1))