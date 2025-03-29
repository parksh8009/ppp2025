def c2f(t_c):
    temp_f=(t_c*9/5)+32
    return temp_f

def main ():
    t_c=int(input('섭씨: '))
    print(f'{t_c}℃는 {c2f(t_c):.2f}℉입니다.')

if __name__ == '__main__':
    main()
