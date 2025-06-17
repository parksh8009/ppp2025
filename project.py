import PySimpleGUI as sg
import random
import time

def generate_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(0, 9))
    return numbers

def show_popup(title, message_lines, button_text="확인", highlight=None):
    layout = []
    for i, line in enumerate(message_lines):
        color = "red" if highlight and i in highlight else None
        layout.append([sg.Text(line, font=("Helvetica", 14), text_color=color, justification='center', expand_x=True)])
    layout.append([sg.Button(button_text, font=("Helvetica", 12), size=(10, 1))])
    window = sg.Window(title, layout, element_justification='center', finalize=True, keep_on_top=True, margins=(30, 20))
    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED or event == button_text:
            break
    window.close()

def memory_game(level):
    numbers = generate_numbers(level + 2)
    number_str = ", ".join(map(str, numbers))

    layout_show = [
        [sg.Text(f"🧠 기억력 게임", font=("Helvetica", 20), justification='center', expand_x=True)],
        [sg.Text(f"레벨 {level}", font=("Helvetica", 16), justification='center', expand_x=True)],
        [sg.Text("이 숫자를 외우세요!", font=("Helvetica", 14), justification='center', expand_x=True)],
        [sg.Text(number_str, font=("Helvetica", 24), text_color='blue', justification='center', expand_x=True)]
    ]
    window = sg.Window("기억력 테스트", layout_show, 
    element_justification='center', finalize=True, keep_on_top=True, margins=(40, 20))
    window.refresh()
    time.sleep(3)
    window.close()

    layout_input = [
        [sg.Text("숫자를 띄어쓰기로 구분하여 입력하세요 (예: 1 2 3)", font=("Helvetica", 13))],
        [sg.InputText(font=("Helvetica", 14), size=(20, 1))],
        [sg.Button("제출", font=("Helvetica", 12), size=(10, 1))]
    ]
    window = sg.Window("답 입력", layout_input, element_justification='center', 
    finalize=True, keep_on_top=True, margins=(30, 20))
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "제출"):
            break
    window.close()

    try:
        user_numbers = [int(x.strip()) for x in values[0].split() if x.strip().isdigit()]
    except:
        return False, numbers

    return user_numbers == numbers, numbers

def main():
    show_popup("🎮 기억력 게임", [
        "기억력 게임에 오신 걸 환영합니다!",
        "숫자를 외우고 입력하는 간단한 게임입니다.",
        "레벨이 올라갈수록 숫자가 많아집니다."
    ], button_text="시작")

    level = 1
    while True:
        success, correct = memory_game(level)
        if success:
            show_popup("🎉 정답입니다!", [f"레벨 {level} 클리어!","다음 단계로 진행합니다."], button_text="계속")
            level += 1
        else:
            show_popup("💀 게임 오버", ["틀렸습니다!",f"정답은: {' '.join(map(str, correct))}",
            f"도달한 최고 레벨: {level}"], button_text="종료", highlight=[0])  
            break

if __name__ == "__main__":
    main()
