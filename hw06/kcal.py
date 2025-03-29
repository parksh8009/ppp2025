def main():
    kcal={'한라봉':50/100, '딸기':34/100, '바나나':77/100}
    total=0
    for fruit in kcal:
        eat=int(input(f'{fruit} 섭취량 (g) : '))
        total+=eat*kcal[fruit]
    print(f'총 섭취 칼로리 : {total:.2f}kcal')
if __name__ == '__main__':
    main()


