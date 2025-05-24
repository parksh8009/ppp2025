import random

def check(solution, answer, input_ch):
    is_correct = False
    for i in range(len(solution)):
        if solution[i] == input_ch:
            answer[i] = solution[i]
            is_correct = True
    return is_correct

def main():
    problems = ["apple", "banana"]
    solution = problems[random.randrange(len(problems))]
    is_correct = False
    lives = 5
    answer = ["_" for _ in solution]

    while True:
        input_ch = input(f"{''.join(answer)}? ")

        if check(solution, answer, input_ch):
            print(f"{input_ch}가 포함되어 있습니다.")
        else:
            lives -= 1
            print(f"{input_ch}는 없습니다. 남은 기회: {lives}")

        if "_" not in answer:
            print("정답입니다. 잘하셨습니다!")
            break

        if lives == 0:
            print(f"기회를 모두 사용했습니다. 정답은 '{solution}'입니다.")
            break

if __name__ == "__main__":
    main()
