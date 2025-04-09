def count(nums):
    return len(nums)

def average(nums):
    return sum(nums) / len(nums)

def minmax(nums):
    return min(nums), max(nums)

def median(nums):
    sorted_list= sorted(nums)
    return sorted_list[len(sorted_list)//2]

def read_numbers(filename):
    nums=[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            nums.append(int(line.strip()))
    return nums

def main():
    nums = read_numbers('numbers.txt')
    print(f'총 숫자의 개수 : {count(nums)}')
    print(f'평균값 : {average(nums):.1f}')
    print(f'최대값 : {max(nums)}')
    print(f'최소값 : {min(nums)}')
    print(f'중앙값 : {median(nums)}')


if __name__ == '__main__':
    main()
