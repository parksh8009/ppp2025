import random
from rich import print
import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(prompt: str) -> str:
    return simpledialog.askstring("로또 추첨기", prompt, parent=window)

def get_lotto():
    lotto_list = []
    while len(lotto_list) < 6:
        num = random.randint(1, 45)
        if num not in lotto_list:
            lotto_list.append(num)
    return lotto_list

def main():
    print("[bold magenta]로또 번호 추첨기입니다![/bold magenta] :game_die:")

    count_input = gui_input("추첨할 횟수를 입력하세요:")
    if count_input is None or not count_input.isdigit():
        print("[red]숫자를 입력하지 않거나 입력값이 잘못되었습니다.[/red]")
        return

    count = int(count_input)

    for i in range(count):
        lotto_num = get_lotto()
        print(f"[bold green]{i+1}회차 번호:[/bold green]", sorted(lotto_num))

if __name__ == "__main__":
    main()
