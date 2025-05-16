import random

# 초성 추출
def to_chosung_ch(ch):
    if '가' <= ch <= '힣':
        return (ord(ch) - ord("가")) // 588
    return ch  # 한글이 아니면 그대로

# 단어 전체 초성으로 바꾸기
def to_chosung(text):
    result = []
    for ch in text:
        if '가' <= ch <= '힣':
            chosung_index = to_chosung_ch(ch)
            CHOSUNG_LIST = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", 
                            "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
            result.append(CHOSUNG_LIST[chosung_index])
        else:
            result.append(ch)
    return ''.join(result)

# 게임 실행 함수
def main():
    problems = ["바나나", "딸기", "토마토", "복숭아"]
    solution = random.choice(problems)
    hint = to_chosung(solution)

    print(f"초성 퀴즈! 제시어: {hint}")
    for i in range(3):
        answer = input("정답은? ")
        if answer == solution:
            print("정답입니다!")
            return
        else:
            print("오답입니다.")
    print(f"게임오버! 정답은 '{solution}'이었습니다.")


if __name__ == "__main__":
    main()