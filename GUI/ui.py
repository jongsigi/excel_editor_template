import tkinter as tk

def create_button(parent, text, command, pady=5):
    """버튼을 생성하는 유틸리티 함수"""
    button = tk.Button(parent, text=text, command=command)
    button.pack(pady=pady)
    return button

def create_label(parent, initial_text="", wraplength=400, height=4):
    """
    라벨을 생성하는 함수
    
    Args:
        parent: 부모 위젯
        initial_text (str): 초기 표시될 텍스트
        wraplength (int): 텍스트 줄바꿈 길이
        height (int): 라벨의 높이
        
    Returns:
        tuple: (label 위젯, StringVar 객체)
    """
    label_var = tk.StringVar()
    label_var.set(initial_text)
    label = tk.Label(parent, textvariable=label_var, wraplength=wraplength, height=height)
    label.pack(pady=10)
    return label, label_var

def create_checkbox_frame(parent):
    """
    체크박스를 담을 프레임을 생성하는 함수
    
    Args:
        parent: 부모 위젯
    
    Returns:
        tuple: (체크박스 프레임, 체크박스 변수 딕셔너리)
    """
    frame = tk.Frame(parent)
    frame.pack(pady=10)
    return frame, {}

def add_checkbox(frame, checkboxes, column):
    """
    체크박스를 하나씩 추가하는 함수
    
    Args:
        frame: 체크박스를 추가할 프레임
        checkboxes: 체크박스 변수 딕셔너리
        column: 추가할 컬럼명
    """
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(frame, text=column, variable=var)
    checkbox.pack(anchor='w')
    checkboxes[column] = var