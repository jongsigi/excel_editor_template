def analyze_column_pattern(df, column):
    """
    컬럼의 데이터 패턴을 분석하는 함수
    
    Args:
        df: DataFrame
        column: 분석할 컬럼명
    
    Returns:
        dict: 패턴 분석 결과
    """
    unique_values = df[column].unique()
    sample_value = str(unique_values[0])
    pattern_info = {
        'column': column,
        'unique_count': len(unique_values),
        'pattern_type': None,
        'structure': None
    }
    
    # JSON/Dictionary 형태 패턴 확인
    if sample_value.count('{') > 0 and sample_value.count('}') > 0:
        pattern_info['pattern_type'] = 'nested_structure'
        try:
            import ast
            # 샘플 값을 파싱하여 구조 확인
            parsed = ast.literal_eval(sample_value)
            pattern_info['structure'] = {
                'type': 'dictionary',
                'depth': str(parsed).count('{'),
                'keys': list(parsed.keys()) if isinstance(parsed, dict) else []
            }
        except:
            pattern_info['structure'] = 'unparseable_dict' 
    
    # 구분자로 나뉜 문자열 패턴 확인
    elif ',' in sample_value:
        parts = sample_value.split(',')
        pattern_info['pattern_type'] = 'delimited'
        pattern_info['structure'] = {
            'delimiter': ',',
            'parts_count': len(parts),
            'sample_parts': [p.strip() for p in parts]
        }
    
    # 공통 접두사/접미사 패턴 확인
    else:
        from difflib import SequenceMatcher
        common_prefix = ''
        common_suffix = ''
        
        # 모든 고유값들 간의 공통 부분 찾기
        for i in range(min(len(s) for s in unique_values)):
            if len(set(v[i] for v in unique_values)) == 1:
                common_prefix += unique_values[0][i]
            else:
                break
                
        pattern_info['pattern_type'] = 'common_parts'
        pattern_info['structure'] = {
            'prefix': common_prefix if common_prefix else None,
            'suffix': common_suffix if common_suffix else None,
            'samples': unique_values[:5].tolist()  # 처음 5개 샘플만 저장
        }
    
    return pattern_info