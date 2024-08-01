import pandas as pd
import re

# 엑셀 파일 읽기
input_file = 'merge3.xlsx'  # 엑셀 파일 경로를 입력하세요
df = pd.read_excel(input_file)

# 특정 문자열을 검색하는 함수
def check_bracket_content(row):
    if pd.isna(row['상행(Y)']):  # '상행(Y)' 열에 데이터가 없을 때만 처리
        # 괄호 사이의 내용을 추출하는 정규식
        if '서울방향' in str(row['충전소명']) or '상행' in str(row['충전소명']) or '서울' in str(row['충전소명']):
            return 'Y'
        bracket_content = re.findall(r'\((.*?)\)', str(row['충전소명']))
        if bracket_content:
            for content in bracket_content:
                if '서울방향' in content or '상행' in content or '서울' in content:
                    return 'Y'
                
        return 'N'
    return row['상행(Y)']  # 이미 데이터가 있는 경우 기존 데이터를 유지

# '상행(Y)' 열 업데이트
df['상행(Y)'] = df.apply(check_bracket_content, axis=1)

# 새로운 데이터셋 저장
output_file = 'merge4.xlsx'  # 결과를 저장할 엑셀 파일 경로
df.to_excel(output_file, index=False)

print(df)
