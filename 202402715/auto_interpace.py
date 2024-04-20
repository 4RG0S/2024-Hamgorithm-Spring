import tkinter as tk
from tkinter import simpledialog, messagebox, font as tkfont
import subprocess
import os

def execute_git_commands(problem_number, problem_name):
    try:
        # 경로 설정
        path = r"C:\Users\becky\OneDrive\문서\GitHub\2024-Hamgorithm-Spring\202402715" # 저장할 경로를 입력해주세요!
        os.chdir(path)

        # git bash 경로
        git_bash_path = "C:/Program Files/Git/git-bash.exe"
        
        # 파일 이름 설정
        file_name = problem_number + ".java"

        # git 명령어 실행
        subprocess.check_call([git_bash_path, "-c", "git switch 202402686"])
        subprocess.check_call([git_bash_path, "-c", f"git add {file_name}"])
        subprocess.check_call([git_bash_path, "-c", f"git commit -m \"{problem_number}번 - {problem_name}\""])
        subprocess.check_call([git_bash_path, "-c", "git push"])
        messagebox.showinfo("성공", "Git 명령어가 성공적으로 실행되었습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"오류가 발생했습니다: {e}")

def on_submit():
    problem_number = problem_number_entry.get()
    problem_name = problem_name_entry.get()
    execute_git_commands(problem_number, problem_name)

# GUI 설정
root = tk.Tk()
root.title("Git push해줄게")

# 폰트 설정
label_font = tkfont.Font(size=14)
entry_font = tkfont.Font(size=12)
button_font = tkfont.Font(size=12)

# 위젯 크기 조정
tk.Label(root, text="문제 번호:", font=label_font).pack(pady=10)
problem_number_entry = tk.Entry(root, font=entry_font)
problem_number_entry.pack(pady=5, padx=10, ipadx=50, ipady=4)

tk.Label(root, text="문제 이름:", font=label_font).pack(pady=10)
problem_name_entry = tk.Entry(root, font=entry_font)
problem_name_entry.pack(pady=5, padx=10, ipadx=50, ipady=4)

submit_button = tk.Button(root, text="제출", command=on_submit, font=button_font)
submit_button.pack(pady=10, ipadx=10, ipady=5)

# 창 크기 설정
root.geometry('400x200')

root.mainloop()
