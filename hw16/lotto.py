
import random

def get_lotto():
    lotto_list=[]
    while True:
        n= random.randint(a=1, b=45)
        if n not in lotto_list:
            lotto_list.append(n)
        if len(lotto_list)==6:
            break
    return sorted(lotto_list)

def main():
    count = int(input("로또 번호를 몇 번 뽑을까요? : "))
    for i in range(count):
        lotto_num = get_lotto()
        print(f"{i+1}회차: {lotto_num}")

if __name__ == "__main__":
    main()
