weight=int(input('몸무게 : '))
height=int(input('키 : '))
height_m=height/100
BMI=weight/(height_m**2)

print('BMI : {}'.format(BMI))
if 23<=BMI<=24.9:
    print('비만 전단계입니다.')
elif 25<=BMI<=29.9:
    print('1단계 비만입니다.')
elif 30<=BMI<=34.9:
    print('2단계 비만입니다.')
elif BMI>=35:
    print('3단계 비만입니다.')
