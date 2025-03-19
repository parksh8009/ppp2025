kcal={'한라봉':50,'딸기':34,'바나나':77}
h=int(input('한라봉 섭취량(g) : '))
s=int(input('딸기 섭취량(g) : '))
b=int(input('바나나 섭취량(g) : '))

total_kcal=(kcal['한라봉']*h/100)+(kcal['딸기']*s/100)+(kcal['바나나']*b/100)
print('총 섭취 칼로리 : {}'.format(total_kcal))