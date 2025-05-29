from rich import print
import tkinter as tk
from tkinter import simpledialog
import time

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

def count_down(count):
    for n in range(count, 0, -1):
        m, s = divmod(n, 60)
        print(f"[bold blue]{m:02d}:{s:02d}[/bold blue]", end="\r")
        time.sleep(1)
    print("[bold magenta]Boooooomb![/bold magenta]")

def main():
    user_input = gui_input("몇 초 동안 타이머를 실행할까요?")
    if user_input and user_input.isdigit():
        count = int(user_input)
        count_down(count)
    else:
        print("[red]유효한 숫자를 입력하지 않았습니다.[/red]")

if __name__ == "__main__":
    main()
