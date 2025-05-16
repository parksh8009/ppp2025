def caesar_encode_ch(ch: str, shift: int) -> str:
    if 'a' <= ch <= 'z':
        return chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= ch <= 'Z':
        return chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    else:
        return ch

def caesar_encode(text: str, shift: int = 3) -> str:
    return ''.join(caesar_encode_ch(ch, shift) for ch in text)

def main():
    text = input("암호화할 문자열을 입력하세요: ")
    result = caesar_encode(text)
    print("암호화 결과:", result)

if __name__ == "__main__":
    main()
