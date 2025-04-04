def average(nums):
    return sum(nums) / len(nums)

def main():
    text_input = input("숫자 여러 개를 ','로 구분하여 입력하세요: ")  
    nums = [int(text) for text in text_input.split(",") ] 
    print(f'평균값은 : {average(nums)}')

if __name__ == '__main__':
    main()





#여러 값을 한 줄로 입력받기 전 코드
def average(nums):
    return sum(nums) / len(nums)

def main():
    text_input = input("숫자 여러 개를 ','로 구분하여 입력하세요: ")
    nums=[]
    for text in text_input.split(','):
        nums.append(int(text))
    print(f'평균값은 : {average(nums)}')

if __name__ == '__main__':
    main()

