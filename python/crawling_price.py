import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# 크롬 드라이버 초기화
driver = webdriver.Chrome()

def get_kakao_map_menu(data):
    # 카카오맵 검색 페이지로 이동
    search_url = f"https://map.kakao.com/?q={data}"
    driver.get(search_url)
    time.sleep(5)  # 페이지가 완전히 로드될 때까지 기다립니다
    print("wait")

    

    try:
		
        # '상세보기' 버튼 클릭
        moreview_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.moreview'))
        )
        moreview_button.click()

        # 메뉴 정보가 있는 div로 이동
        menu_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-viewid="menuInfo"]'))
        )

        # 메뉴 가격 정보 크롤링
        menu_items = menu_div.find_elements(By.CLASS_NAME, 'price_menu')
        menu_texts = []
        for item in menu_items:
            price = item.text.replace('가격: ', '').strip()
            menu_texts.append(price)

        return "\n".join(menu_texts)
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return '오류 발생'

# 데이터 읽기
excel = pd.read_excel('final_labeled.xlsx')
book = excel[excel['VISIT_AREA_TYPE_CD'] == 11]

# 메뉴 정보를 저장할 리스트
menus = []
for area in book['VISIT_AREA_NM']:
    menu_info = get_kakao_map_menu(area)
    menus.append(menu_info)

# 메뉴 정보를 데이터프레임에 추가
book['메뉴 정보'] = menus

# 결과를 엑셀 파일로 저장
book.to_excel('menu_search_results_kakao.xlsx', index=False)
print("Menu search results saved to menu_search_results_kakao.xlsx")

# 드라이버 종료
driver.quit()