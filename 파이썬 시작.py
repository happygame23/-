from tkinter import *
import random

# 전역 변수
answer = random.randint(1, 100)
attempt_count = 0
colors = ["pink", "lightblue", "lightgreen", "yellow", "orange"]
rankings = []  # 랭킹 기록 (도전자 이름, 점수)