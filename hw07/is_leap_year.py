def is_leap_year(y):
    if y % 4 == 0 and y % 100 !=0:
        return True
    else:
        return False
        

def main():
    y=int(input('년도를 입력하시오 : '))
    print(is_leap_year(y))


if __name__ == '__main__':
    main()