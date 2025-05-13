def str2int(text: str, default_value: int = -999) -> int:
    try:
        return int(text)
    except ValueError:
        print(f"에러났어요...! {text}")
        return default_value

def main():
    numbers = []
    
    while True:
        user_input = input("X=?")
        value = str2int(user_input)
        
        if value == -1:
            break
        elif value > 0:
            numbers.append(value)

    if len(numbers) > 0:
        avg = sum(numbers) / len(numbers)
        print(f"입력된 값은 {numbers} 입니다. 총 {len(numbers)}개의 자연수가 입력되었고, 평균은 {avg:.1f}입니다.")
    else:
        print("자연수가 입력되지 않았습니다.")

if __name__ == "__main__":
    main()
