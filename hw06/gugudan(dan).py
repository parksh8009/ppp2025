def gugudan(dan):
    for i in range(1,10):
        print(f'{dan}X{i}={dan*i}')
def main():
    dan=int(input('몇 단을 출력할까요? : '))
    gugudan(dan)

if __name__ == '__main__':
    main()
