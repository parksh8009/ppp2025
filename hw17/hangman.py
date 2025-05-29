import random
from rich import print

def check(solution, answer, input_ch):
    is_correct = False
    for i in range(len(solution)):
        if solution[i] == input_ch:
            answer[i] = input_ch
            is_correct = True
    return is_correct

def main():
    word_list = ["apple", "banana", "orange", "grape"]
    solution = list(random.choice(word_list))
    answer = ["_"] * len(solution)
    lives = 7

    print("[bold cyan]★ 단어 맞추기 게임을 시작합니다![/bold cyan] :game_die:")

    while True:
        print(" ".join(answer), f"[dim](lives={lives})[/dim]")
        input_ch = input("답을 입력하시오 => ").lower()

        if len(input_ch) != 1 or not input_ch.isalpha():
            print("[yellow]한 글자의 알파벳만 입력해주세요.[/yellow] :warning:")
            continue

        is_correct = check(solution, answer, input_ch)

        if not is_correct:
            print("[red]틀렸습니다.[/red] :x:")
            lives -= 1
        else:
            print("[green]맞았습니다![/green] :white_check_mark:")

        if "_" not in answer:
            print("[bold green]정답입니다! 잘하셨습니다![/bold green] :tada:")
            break

        if lives == 0:
            print("[bold red]게임오버. 다시 시도하세요.[/bold red] :skull:")
            print(f"[magenta]정답은: {''.join(solution)}[/magenta]")
            break

if __name__ == "__main__":
    main()