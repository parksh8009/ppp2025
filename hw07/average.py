def average(nums):
    return sum(nums)/len(nums)

def main():
    nums=[5,7,22,11,3,2,30,14,75,74]
    print(f'평균값은 : {average(nums):.1f}')

if __name__ == '__main__':
    main()


