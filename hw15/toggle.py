def toggle_text(text: str) -> str:
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr(ord(ch) - 32))  # 소문자 → 대문자
        elif 'A' <= ch <= 'Z':
            result.append(chr(ord(ch) + 32))  # 대문자 → 소문자
        else:
            result.append(ch)  # 알파벳 아닌 문자
    return ''.join(result)

def main():
    sample=input("영문자 입력 : ")
    print("변환 결과:", toggle_text(sample))  # hELLO pYTHON!

if __name__ == "__main__":
    main()
