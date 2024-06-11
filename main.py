import threading
import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

아이디 = ''
비밀번호 = ''
로그인페이지 = 'https://etk.srail.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000'
조회페이지 = 'https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000'
출발지 = '수서'
도착지 = '대전'


def open_webdriver():
    # 크롬드라이버
    크롬드라이버다운로드 = chromedriver_autoinstaller.install(cwd=True)
    driver = webdriver.Chrome(크롬드라이버다운로드)

    try:
        # 로그인
        driver.get(로그인페이지)
        driver.find_element(By.ID, 'srchDvNm01').send_keys(아이디)
        driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys(비밀번호)
        driver.find_element(By.XPATH, "//input[@value='확인']").click()
        time.sleep(0.1)
        driver.get(조회페이지)

        # 무한반복
        while True:
            driver.execute_script("window.scrollTo(0, 0)")
            driver.get(조회페이지)

            # 날짜선택 (option 뒤 숫자 조정)
            driver.find_element(By.ID, 'dptDt').click()  # 4, 8
            driver.find_element(By.XPATH, '//*[@id="dptDt"]/option[4]').click()

            # 시간선택 (option 뒤 숫자 조정)
            driver.find_element(By.ID, 'dptTm').click()
            driver.find_element(By.XPATH, '//*[@id="dptTm"]/option[8]').click()

            # 출발지 도착지 지정
            driver.find_element(By.ID, 'dptRsStnCdNm').clear()
            driver.find_element(By.ID, 'arvRsStnCdNm').clear()
            driver.find_element(By.ID, 'dptRsStnCdNm').send_keys(출발지)
            driver.find_element(By.ID, 'arvRsStnCdNm').send_keys(도착지)

            # 조회하기 클릭
            driver.find_element(By.XPATH, "//input[@value='조회하기']").click()

            # 대기열 패스
            while True:
                # 기다릴 최대 시간 (초)
                wait_time = 100
                wait = WebDriverWait(driver, wait_time)

                try:
                    wait.until(EC.presence_of_element_located((By.LINK_TEXT, '매진')))
                    break
                except:
                    continue

            # 예약 버튼 찾아서 클릭
            for i in range(1, 11):  # 1부터 10까지 반복 (첫번째줄 ~ 10번째줄)
                try:
                    예약버튼 = driver.find_element(By.XPATH,f'//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[{i}]/td[7]/a')
                    if 예약버튼.text == '예약하기':
                        print(f"{i}번째 빈자리 발견")
                        try:
                            예약버튼.click()
                            time.sleep(2)
                            driver.back()
                            break
                        except Exception as e:
                            print(f"{i}번째 예약 중 에러: {e}")
                except Exception as e:
                    print(f"{i}번째 예약 버튼 찾기 실패: {e}")

    finally:
        driver.quit()


# 쓰레드 갯수 지정
num_threads = 1
threads = []

# 쓰레드 돌리기
for _ in range(num_threads):
    thread = threading.Thread(target=open_webdriver)
    threads.append(thread)
    thread.start()

# 쓰레드 대기
for thread in threads:
    thread.join()
