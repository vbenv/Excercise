import pandas as pd
import re

# 엑셀 파일 읽기
input_file = 'output_excel_file8_1.xlsx'  # 엑셀 파일 경로를 입력하세요
df = pd.read_excel(input_file)

# 주소 열에서 괄호와 그 안의 내용을 제거하는 함수
def remove_parentheses(address):
    return re.sub(r'\s*\(.*?\)\s*', '', address)

# C열의 '주소' 열에서 괄호 제거
df['충전소명'] = df['충전소명'].apply(remove_parentheses)

# 수정된 데이터셋 저장
output_file = 'output_excel_file8_2.xlsx'  # 결과를 저장할 엑셀 파일 경로
df.to_excel(output_file, index=False)
