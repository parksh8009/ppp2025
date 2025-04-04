def total_calorie(fruits, fruits_calorie_dic):
    total = 0
    for fruit, weight in fruits.items(): 
        total += (fruits_calorie_dic[fruit] * weight)
    return total

def main():
    fruits = {"딸기": 300, "한라봉": 150}
    fruits_calorie_dic = {'한라봉': 50/100, "딸기": 34/100, '바나나': 77/100}
    print(f'총 섭취 칼로리는 {total_calorie(fruits, fruits_calorie_dic)} kcal 입니다.')

if __name__ == '__main__':
    main()