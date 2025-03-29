def sum_m(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total

def main():
    n=int(input('숫자를 입력하세요 : '))
    print(f'1부터 {n}까지의 합 : {sum_m(n)}')

if __name__ == '__main__':
    main()

