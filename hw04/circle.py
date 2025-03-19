import math
r=int(input('반지름 : '))
circumference=2*math.pi*r
area=math.pi*r**2

print(f'원의 둘레 : {circumference:.1f}')
print(f'원의 면적 : {area:.2f}')