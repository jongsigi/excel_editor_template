import tkinter as tk
from tkinter import ttk
from GUI.ui import *
from utils.utils import *
from utils.FA import *
import pandas as pd
from tkinter import filedialog

class Mode2UI:
    def __init__(self, root):
        self.root = root
        self.selected_file_path_2 = None 
        self.df = None
        
        # 레이블 생성
        self.title = ttk.Label(root, text="2번 UI입니다")
        self.label, self.label_var = create_label(root, "파일을 선택해주세요.")
        
        # 2번째 파일 선택 버튼
        self.file_button = create_button(root, "파일 선택", self.on_select_file)

        # 실행 버튼
        self.run_button = create_button(root, "Run", self.run_files)

        # 체크박스 프레임 초기화
        self.checkbox_frame, self.checkboxes = create_checkbox_frame(root)

        # 초기에 모든 위젯 숨기기
        self.hide_widgets()
        
        # 초기에는 숨김 상태
        self.hide_widgets()
        
    def hide_widgets(self):
        self.label.pack_forget()
        self.file_button.pack_forget()
        self.run_button.pack_forget()
        self.checkbox_frame.pack_forget()

    def show_widgets(self):
        self.label.pack(pady=10)
        self.file_button.pack(pady=5)
        self.run_button.pack(pady=5)
        self.checkbox_frame.pack(pady=10, fill='both', expand=True)

    def on_select_file(self):
        path = select_file_path()
        if path:
            self.selected_file_path_2 = path
            self.label_var.set(f"파일 선택됨: {path}")
        else:
            self.label_var.set("파일이 선택되지 않았습니다.")

    def run_files(self):
        if not self.selected_file_path_2:
            return

        df = excel_to_df(self.selected_file_path_2)
        self.df = df
        self.label_var.set(f"파일이 성공적으로 로드되었습니다: {self.selected_file_path_2}")

        df = add_column_to_df(df)
        self.nan_df, self.not_nan_df = split_by_nan(df, 'fail_dft_image')
        self.nan_df = self.nan_df.copy()  # row별 수정 위해 복사
        self.nan_df = nan_df_edit(self.nan_df)

        # 기존 체크박스/버튼 제거
        for widget in self.checkbox_frame.winfo_children():
            widget.destroy()
        self.checkboxes.clear()

        # not_nan_df 인덱스 리스트 및 포인터 초기화
        self.not_nan_indices = list(self.not_nan_df.index)
        self.current_not_nan_idx = 0

        # 첫 번째 row 버튼 표시
        self.show_next_not_nan_row_buttons()

    def show_next_not_nan_row_buttons(self):
        # 기존 row_frame 제거
        for widget in self.checkbox_frame.winfo_children():
            widget.destroy()

        if self.current_not_nan_idx < len(self.not_nan_indices):
            idx = self.not_nan_indices[self.current_not_nan_idx]
            row = self.not_nan_df.loc[idx]

            row_frame = ttk.Frame(self.checkbox_frame)
            row_frame.pack(fill='x', pady=2)

            ttk.Label(row_frame, text=f"index: {idx}, fail_mode: {row['fail_mode']}").pack(side='left', padx=5)

            ttk.Button(row_frame, text="SCT", command=lambda: self.set_not_nan_row_value(idx, '하부 Metal Layer Crack', 'SCT Crack')).pack(side='left', padx=2)
            ttk.Button(row_frame, text="Nand Chip Crack", command=lambda: self.set_not_nan_row_value(idx, 'Nand Chip Crack', 'Nand Chip crack')).pack(side='left', padx=2)
            ttk.Button(row_frame, text="X-dec", command=lambda: self.set_not_nan_row_value(idx, 'Nand Chip Crack (X-dec)', 'Nand Chip Crack')).pack(side='left', padx=2)
            ttk.Button(row_frame, text="기타", command=lambda: self.set_not_nan_row_value(idx, '기타', '기타')).pack(side='left', padx=2)
        else:
            ttk.Label(self.checkbox_frame, text="모든 행 처리가 완료되었습니다.").pack(pady=10)
            # 저장 버튼 추가
            ttk.Button(self.checkbox_frame, text="엑셀로 저장", command=self.save_to_excel).pack(pady=10)

    def set_not_nan_row_value(self, idx, fail_type, fail_type_cat):
        self.not_nan_df.at[idx, 'fail_type'] = fail_type
        self.not_nan_df.at[idx, 'fail_type_cat'] = fail_type_cat
        self.label_var.set(f"index {idx} 처리 완료: {fail_type} / {fail_type_cat}")
        self.current_not_nan_idx += 1
        self.show_next_not_nan_row_buttons()

    def save_to_excel(self):
        # 두 데이터프레임 합치기
        result_df = pd.concat([self.nan_df, self.not_nan_df]).sort_index()
        # 파일 저장 다이얼로그
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            result_df.to_excel(file_path, index=False)
            self.label_var.set(f"엑셀로 저장 완료: {file_path}")
        else:
            self.label_var.set("저장이 취소되었습니다.")
