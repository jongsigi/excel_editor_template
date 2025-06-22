# FA에 필요한 기능은 여기에 작성합니다.
# 이 파일은 utils 폴더에 위치합니다.
# 기능 1 : 특정 column null 경우, 다른 column에 조건에 맞춰 값을 추가
# 기능 2 : 특정 column not_null 경우, 버튼 클릭에 따라 다른 column에 조건에 맞춰 값을 추가
import pandas as pd

def add_column_to_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    기존 DataFrame에 'fail_type'과 'fail_type_cat' 컬럼을 추가합니다.
    초기값은 모두 None으로 설정됩니다.

    Args:
        df (pd.DataFrame): 원본 데이터프레임

    Returns:
        pd.DataFrame: 컬럼이 추가된 데이터프레임
    """
    df['fail_type'] = None
    df['fail_type_cat'] = None
    return df

def split_by_nan(df: pd.DataFrame, column: str):
    """
    특정 column이 NaN인 데이터프레임과 값이 있는 데이터프레임으로 분리합니다.

    Args:
        df (pd.DataFrame): 원본 데이터프레임
        column (str): 기준이 되는 컬럼명

    Returns:
        tuple: (nan_df, not_nan_df)
            nan_df: column이 NaN인 행만 포함하는 데이터프레임
            not_nan_df: column이 NaN이 아닌 행만 포함하는 데이터프레임
    """
    nan_df = df[df[column].isna()]
    not_nan_df = df[df[column].notna()]
    return nan_df, not_nan_df
    
def nan_df_edit(nan_df: pd.DataFrame) -> pd.DataFrame:
    """
    fail_mode 컬럼 값에 따라 fail_type, fail_type_cat 컬럼 값을 추가합니다.
    - fail_mode == 'pass' : fail_type = 'GIB', fail_type_cat = 'GIB'
    - fail_mode == 'NVD'  : fail_type = 'NVD', fail_type_cat = 'NVD'
    """
    nan_df = nan_df.copy()
    nan_df.loc[nan_df['fail_mode'] == 'pass', ['fail_type', 'fail_type_cat']] = ['GIB', 'GIB']
    nan_df.loc[nan_df['fail_mode'] == 'NVD',  ['fail_type', 'fail_type_cat']] = ['NVD', 'NVD']
    return nan_df