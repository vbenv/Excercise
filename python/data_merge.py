# import pandas as pd

# # 엑셀 파일 읽기
# file1 = 'output_excel_file6_1.xlsx'  # 첫 번째 엑셀 파일 경로
# file2 = 'output_excel_file7.xlsx'  # 두 번째 엑셀 파일 경로

# df1 = pd.read_excel(file1)
# df2 = pd.read_excel(file2)

# # 두 데이터프레임을 충전소명을 기준으로 병합
# def check_lon(row):
#     if pd.isna(row['Iat']):  # '상행(Y)' 열에 데이터가 없을 때만 처리
#         # 괄호 사이의 내용을 추출하는 정규식
#         if '서울방향' in str(row['충전소명']) or '상행' in str(row['충전소명']) or '서울' in str(row['충전소명']):
#             return 'Y'
#         bracket_content = re.findall(r'\((.*?)\)', str(row['충전소명']))
#         if bracket_content:
#             for content in bracket_content:
#                 if '서울방향' in content or '상행' in content or '서울' in content:
#                     return 'Y'
                
#         return 'N'
#     return row['상행(Y)']  # 이미 데이터가 있는 경우 기존 데이터를 유지
# merged_df = pd.merge(df1, df2, on='충전소명', how='left')

# # 병합된 결과를 새로운 엑셀 파일로 저장
# output_file = 'merged_output.xlsx'  # 결과를 저장할 엑셀 파일 경로
# merged_df.to_excel(output_file, index=False)

# print(merged_df)
# # import pandas as pd

# # # 엑셀 파일 읽기
# # input_file = 'merge2.xlsx'  # 엑셀 파일 경로를 입력하세요
# # df = pd.read_excel(input_file)

# # # G열이 비어있는지 확인하고, 비어있는 경우 I:K열의 내용을 G열로 옮기기
# # def move_columns(row):
# #     if pd.isna(row['I']):
# #         row['I'] = row['K']
# #     return row

# # # G열 업데이트
# # df = df.apply(move_columns, axis=1)

# # # 결과 저장
# # output_file = 'merge3.xlsx'  # 결과를 저장할 엑셀 파일 경로
# # df.to_excel(output_file, index=False)

# # print(df)

# import pandas as pd

# # 엑셀 파일 읽기
# file1 = 'merge4.xlsx'  # 첫 번째 엑셀 파일 경로
# file2 = '충전소 리스트-20240526215827.xlsx'  # 두 번째 엑셀 파일 경로

# df1 = pd.read_excel(file1)
# df2 = pd.read_excel(file2)

# # "Iat" 열이 비어있는 경우에만 업데이트하는 함수
# def update_lat_lon(row):
#     if pd.isna(row['Iat']):
#         matching_row = df2[df2['소재지 도로명 주소'] == row['주소_x']]
#         if not matching_row.empty:
#             row['Iat'] = matching_row.iloc[0]['위도']
#             row['Ion'] = matching_row.iloc[0]['경도']
#     return row

# # 각 행에 대해 함수 적용
# df1 = df1.apply(update_lat_lon, axis=1)

# # 결과 저장
# df1.to_excel('merge4_1.xlsx', index=False)

# print(df1)

import pandas as pd
import re

# 엑셀 파일 읽기
input_file = 'merge4.xlsx'  # 엑셀 파일 경로를 입력하세요
df = pd.read_excel(input_file)

# 고속도로 이름을 추출하여 매핑하는 함수
def extract_highway_name(address):
    if pd.isna(address):
        return None
    # 정규 표현식을 사용하여 "xx고속" 패턴 찾기
    match = re.search(r'(\S+고속)', address)
    if match:
        highway_name = match.group(1) + "도로"
        return highway_name
    return "알 수 없음"

# 새로운 열 추가
df['위치한 고속도로 명'] = df['주소_x'].apply(extract_highway_name)

# 결과 저장
output_file = 'merge5.xlsx'  # 결과를 저장할 엑셀 파일 경로
df.to_excel(output_file, index=False)

print(df)
