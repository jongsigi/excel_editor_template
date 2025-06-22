import tkinter as tk
from tkinter import ttk
from GUI.Mode1UI import Mode1UI
from GUI.Mode2UI import Mode2UI

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("파일 선택기")
        self.root.geometry("800x400")

        # 모드 선택 변수
        self.mode_var = tk.StringVar()
        
        # 모드 UI 인스턴스
        self.mode1_ui = Mode1UI(root)
        self.mode2_ui = Mode2UI(root)
        
        # 선택박스 생성
        self.create_mode_selector()

    def create_mode_selector(self):
        selector_frame = ttk.Frame(self.root)
        selector_frame.pack(pady=10)

        ttk.Label(selector_frame, text="모드 선택:").pack(side='left', padx=5)

        mode_combo = ttk.Combobox(selector_frame, 
                                 textvariable=self.mode_var,
                                 values=["선택하세요", "1번 모드", "2번 모드"],
                                 state="readonly")
        mode_combo.pack(side='left', padx=5)
        mode_combo.set("선택하세요")
        
        mode_combo.bind('<<ComboboxSelected>>', self.on_mode_change)

    def on_mode_change(self, event):
        selected_mode = self.mode_var.get()
        
        # 모든 모드 UI 숨기기
        self.mode1_ui.hide_widgets()
        self.mode2_ui.hide_widgets()
        
        # 선택된 모드에 따라 UI 표시
        if selected_mode == "1번 모드":
            self.mode1_ui.show_widgets()
        elif selected_mode == "2번 모드":
            self.mode2_ui.show_widgets()