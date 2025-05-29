import tkinter as tk
from tkinter import simpledialog
import random
from rich import print

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="구구단 퀴즈", prompt=text, parent=window)

def problem():
    dan = random.randint(2, 9)
    mul = random.randint(1, 9)

    ans = gui_input(f"{dan} x {mul} = ?")
    if ans is None or not ans.isdigit():
        print("[yellow]숫자만 입력해주세요.[/yellow]")
        return False

    if int(ans) == dan * mul:
        print("[green]정답[/green]")
        return True
    else:
        print(f"[red]오답: 정답은 {dan * mul}입니다.[/red]")
        return False

def main():
    total_problem = 5
    score = 0

    for n in range(total_problem):
        is_correct = problem()
        if is_correct:
            score += 5

    print(f"[bold cyan]총점은 {score}점, {(score / (total_problem * 5)) * 100:.1f}점 입니다.[/bold cyan]")

if __name__ == "__main__":
    main()
