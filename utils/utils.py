from tkinter import filedialog
import pandas as pd

def select_file_path(filetypes=(("모든 파일", "*.*"),)):
    """
    사용자가 파일을 선택하면 절대 경로를 반환한다.
    
    filetypes: 튜플 목록으로 파일 타입 필터 설정 가능.
               예: (("텍스트 파일", "*.txt"), ("모든 파일", "*.*"))
    """
    file_selected = filedialog.askopenfilename(filetypes=filetypes)
    return file_selected

def excel_to_df(file_path):
    """
    엑셀 파일을 읽어 DataFrame으로 변환한다.
    
    file_path: 엑셀 파일의 경로
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"엑셀 파일을 읽는 중 오류 발생: {e}")
        return None