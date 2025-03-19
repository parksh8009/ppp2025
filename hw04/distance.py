import math
x1=0
y1=0
x2=1
y2=0

distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
if distance>1:
    print('거리가 1보다 큽니다.')
elif distance==1:
    print('거리가 1입니다.')
else:
    print('거리가 1보다 작습니다.')
print(distance)