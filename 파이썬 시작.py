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
    
# 점수 계산 및 랭킹 업데이트
def calculate_score(username):
    global rankings
    score = max(100 - attempt_count, 0)  # 시도 횟수가 많을수록 점수는 적어짐
    rankings.append((username, score))
    rankings = sorted(rankings, key=lambda x: -x[1])  # 점수 순 정렬
    update_rankings()

# 랭킹 업데이트 함수
def update_rankings():
    rankingText = "\n".join([f"{i + 1}. {name} - {score}" for i, (name, score) in enumerate(rankings)])
    rankingLabel["text"] = f"랭킹:\n{rankingText}"

# 랭킹 보기 함수
def show_rankings():
    update_rankings()
    rankingWindow.deiconify()
    
# 힌트 제공 함수
def give_hint():
    hint_min = max(1, answer - 10)
    hint_max = min(100, answer + 10)
    hintLabel["text"] = f"힌트: {hint_min} ~ {hint_max}"


# 애니메이션 함수 (공과 풍선)
def animate_ball_and_balloons():
    global ball_x, ball_dx, balloon_x_left, balloon_x_right, balloon_dx_left, balloon_dx_right

    # 공 애니메이션 (왼쪽, 오른쪽 끝에 닿으면 방향 반전)
    if ball_x + 20 > 600 or ball_x - 20 < 0:
        ball_dx = -ball_dx
    ball_x += ball_dx
    canvas_bottom.delete("ball")  # 이전 공 지우기
    canvas_bottom.create_oval(ball_x - 20, ball_y - 20, ball_x + 20, ball_y + 20, fill="red", tags="ball")

    # 왼쪽에서 오른쪽으로 날아가는 풍선
    if balloon_x_left + 40 > 600:  # 풍선이 화면 오른쪽 끝에 닿으면 왼쪽으로 방향 반전
        balloon_dx_left = -balloon_dx_left
    balloon_x_left += balloon_dx_left
    canvas_bottom.delete("balloon_left")  # 이전 풍선 지우기
    canvas_bottom.create_oval(balloon_x_left, balloon_y, balloon_x_left + 40, balloon_y + 60, fill="blue", tags="balloon_left")

    # 오른쪽에서 왼쪽으로 날아가는 풍선
    if balloon_x_right - 40 < 0:  # 풍선이 화면 왼쪽 끝에 닿으면 오른쪽으로 방향 반전
        balloon_dx_right = -balloon_dx_right
    balloon_x_right += balloon_dx_right
    canvas_bottom.delete("balloon_right")  # 이전 풍선 지우기
    canvas_bottom.create_oval(balloon_x_right - 40, balloon_y, balloon_x_right, balloon_y + 60, fill="green", tags="balloon_right")

    # 50ms마다 애니메이션 갱신
    window.after(50, animate_ball_and_balloons)

    
# 게임 초기화 함수
def reset_game():
    global answer, attempt_count
    answer = random.randint(1, 100)
    attempt_count = 0
    resultLabel["text"] = ""
    hintLabel["text"] = ""
    attemptLabel["text"] = "시도 횟수: 0"
    guessField.delete(0, END)

# 캔버스 색상 변경 함수
def change_canvas_color():
    color = random.choice(colors)
    canvas_bottom.config(bg=color)
    window.after(30000, change_canvas_color)  # 30초마다 실행

