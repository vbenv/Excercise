import pandas as pd
import requests

# 엑셀 파일 읽기
input_file = 'output_excel_file8_4.2.xlsx'  # 엑셀 파일 경로를 입력하세요
df = pd.read_excel(input_file)

# 새로운 열 추가
df['lat'] = None
df['lon'] = None

# Geocode API 호출 함수
def get_lat_lon(address):
    url = f'https://geocode.maps.co/search?q={address}&api_key=6651c7c09086b764869378vngf82e15'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['lat'], data[0]['lon']
    return None, None

# 주소 목록에 대해 위도와 경도 가져오기
for index, row in df.iterrows():
    address = row['충전소명']  # C열에 있는 주소를 읽기
    if pd.notna(address):  # 주소가 비어 있지 않은 경우에만 처리
        lat, lon = get_lat_lon(address)
        df.at[index, 'lat'] = lat
        df.at[index, 'lon'] = lon

# 새로운 데이터셋 저장
output_file = 'output_excel_file8_4.3.xlsx'  # 결과를 저장할 엑셀 파일 경로
df.to_excel(output_file, index=False)
