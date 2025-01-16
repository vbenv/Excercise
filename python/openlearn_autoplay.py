from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Selenium 웹 드라이버 설정
driver = webdriver.Chrome()

# 로그인 페이지로 이동
# driver.get("https://openlearn.inha.ac.kr/login/index.php")

# 로그인 자동화 (로그인 폼의 id 값으로 대체)
# username_input = driver.find_element(By.ID, "username")
# password_input = driver.find_element(By.ID, "password")

# username_input.send_keys("your_username")  # 사용자명 입력
# password_input.send_keys("your_password")  # 비밀번호 입력

# login_button = driver.find_element(By.ID, "loginbtn")
# login_button.click()

# 강의 페이지로 이동
driver.get("https://openlearn.inha.ac.kr/course/view.php?id=61")

# 재생 버튼을 순차적으로 클릭하는 매크로
video_buttons = driver.find_elements(By.CLASS_NAME, "instancename")  # 실제 클래스 이름으로 대체

for button in video_buttons:
    button.click()
    
    # 새 창으로 전환
    driver.switch_to.window(driver.window_handles[1])

    # 동영상이 끝날 때까지 대기 (시간 조정 필요)
    time.sleep(300)  # 예시로 5분 대기

    # 창 닫기
    driver.close()

    # 원래 창으로 돌아가기
    driver.switch_to.window(driver.window_handles[0])

driver.quit()
