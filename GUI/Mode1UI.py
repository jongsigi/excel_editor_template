import tkinter as tk
from tkinter import ttk
from utils.utils import *
from utils.datatype import *
from GUI.ui import *

class Mode1UI:
    def __init__(self, root):
        self.root = root
        self.selected_file_path_1 = None 
        self.df = None

        # 라벨 생성
        self.title = ttk.Label(root, text="1번 UI입니다")
        self.label, self.label_var = create_label(root, "파일을 선택해주세요.")
        
        # 첫 번째 파일 선택 버튼
        self.file_button_1 = create_button(root, "파일 선택", self.on_select_file_1)

        # 실행 버튼
        self.run_button = create_button(root, "Run", self.run_files)

        # 체크박스 프레임 초기화
        self.checkbox_frame, self.checkboxes = create_checkbox_frame(root)

        # 초기에 모든 위젯 숨기기
        self.hide_widgets()

    def hide_widgets(self):
        self.label.pack_forget()
        self.file_button_1.pack_forget()
        self.run_button.pack_forget()
        self.checkbox_frame.pack_forget()

    def show_widgets(self):
        self.label.pack(pady=10)
        self.file_button_1.pack(pady=5)
        self.run_button.pack(pady=5)
        self.checkbox_frame.pack(pady=10, fill='both', expand=True)

    def on_select_file_1(self):
        path = select_file_path()
        if path:
            self.selected_file_path_1 = path
            self.label_var.set(f"파일 선택됨: {path}")
        else:
            self.label_var.set("파일이 선택되지 않았습니다.")

    def run_files(self):
        if not self.selected_file_path_1:
            return
            
        df = excel_to_df(self.selected_file_path_1)
        self.df = df
        self.label_var.set(f"파일이 성공적으로 로드되었습니다: {self.selected_file_path_1}")

        # 기존 체크박스들 제거
        for widget in self.checkbox_frame.winfo_children():
            widget.destroy()
        self.checkboxes.clear()
        
        # 컬럼별로 체크박스 추가
        for column in df.columns:
            pattern_info = analyze_column_pattern(df, column)
            if pattern_info['pattern_type']:
                display_name = f"{column} ({pattern_info['pattern_type']})"
            else:
                display_name = column
            add_checkbox(self.checkbox_frame, self.checkboxes, display_name)