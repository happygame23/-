from tkinter import *
import random

# 전역 변수
answer = random.randint(1, 100)
attempt_count = 0
colors = ["pink", "lightblue", "lightgreen", "yellow", "orange"]
rankings = []  # 랭킹 기록 (도전자 이름, 점수)

# 숫자 맞추기 함수
def guessing():
    global attempt_count
    guess = int(guessField.get())
    username = nameField.get()

    if not username.strip():
        resultLabel["text"] = "도전자 이름을 입력하세요!"
        return

    attempt_count += 1

    # 정답 비교
    if guess > answer:
        msg = "정답보다 높음!"
    elif guess < answer:
        msg = "정답보다 낮음!"
    else:
        msg = f"{username}님, 정답입니다!"
        calculate_score(username)
        reset_game()

    resultLabel["text"] = msg
    attemptLabel["text"] = f"시도 횟수: {attempt_count}"
    guessField.delete(0, END)