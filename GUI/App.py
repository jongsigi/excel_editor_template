import tkinter as tk
from utils.utils import *
from GUI.ui import *

class FileSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("파일 선택기")
        # 창 크기 설정 (기본값: 400x200)
        self.root.geometry("800x400")

        self.selected_file_path_1 = None 
        self.df = None

        # 라벨 생성
        self.label, self.label_var = create_label(root, "파일을 선택해주세요.")
        
        # 첫 번째 파일 선택 버튼
        self.file_button_1 = create_button(root, "첫 번째 파일 선택", self.on_select_file_1)

        # 실행 버튼
        self.run_button = create_button(root, "Run", self.run_files)

        # 체크박스 프레임 초기화
        self.checkbox_frame, self.checkboxes = create_checkbox_frame(root)

    def on_select_file_1(self):
        # 첫 번째 파일 선택 대화상자 열기
        path = select_file_path()
        if path:
            self.selected_file_path_1 = path
            self.label_var.set(f"첫 번째 파일 선택됨: {path}")
        else:
            self.label_var.set("첫 번째 파일이 선택되지 않았습니다.")

    def run_files(self):
        # 두 파일 경로를 확인하고 처리
        if self.selected_file_path_1:
            df = excel_to_df(self.selected_file_path_1)
            self.df = df
            self.label_var.set(f"파일이 성공적으로 로드되었습니다: {self.selected_file_path_1}")

             # 기존 체크박스들 제거
            for widget in self.checkbox_frame.winfo_children():
                widget.destroy()
            self.checkboxes.clear()
            
            # 컬럼별로 체크박스 추가
            for column in df.columns:
                add_checkbox(self.checkbox_frame, self.checkboxes, column)
            print(self.df)
            print(f"첫 번째 파일: {self.selected_file_path_1}")