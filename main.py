import threading
import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()


def open_webdriver():
    driver = webdriver.Chrome('C:/Users/aclie/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe',
                              options=chrome_options)

    url = 'https://etk.srail.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000'
    driver.get(url)
    id = '아이디'
    pw = '비밀번호'

    driver.find_element_by_xpath("//input[@id='srchDvNm01']").send_keys(id)
    driver.find_element_by_xpath("//input[@id='hmpgPwdCphd01']").send_keys(pw)
    driver.find_element_by_xpath("//input[@value='확인']").click()

    time.sleep(0.1)

    url2 = 'https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000'
    driver.get(url2)

    while True:
        driver.execute_script("window.scrollTo(0, 0)")
        driver.get(url2)
        start = '수서'
        end = '동대구'

        # 날짜선택
        driver.find_element_by_xpath('//*[@id="dptDt"]').click()
        driver.find_element_by_xpath('//*[@id="dptDt"]/option[1]').click()

        # 시간선택
        driver.find_element_by_xpath('//*[@id="dptTm"]').click()
        driver.find_element_by_xpath('//*[@id="dptTm"]/option[4]').click()

        # 출발지 도착지 지정
        driver.find_element_by_xpath("//input[@id='dptRsStnCdNm']").clear()
        driver.find_element_by_xpath("//input[@id='arvRsStnCdNm']").clear()
        driver.find_element_by_xpath("//input[@id='dptRsStnCdNm']").send_keys(start)
        driver.find_element_by_xpath("//input[@id='arvRsStnCdNm']").send_keys(end)

        # 조회하기 클릭
        driver.find_element_by_xpath("//input[@value='조회하기']").click()
        while True:
            # 기다릴 최대 시간 (초)
            wait_time = 100

            wait = WebDriverWait(driver, wait_time)

            try:
                wait.until(EC.presence_of_element_located((By.LINK_TEXT, '매진')))
                break
            except:
                continue

        search_reservation = driver.find_elements_by_css_selector("div.tbl_wrap.th_thead > table > tbody > tr> td > a")
        for r in search_reservation:
            # print(r.text)
            if r.text == '예약하기':
                print("빈자리 발견")
                # print("빈좌석 발견 예약을 시작합니다 특실일 경우 패스")
                try:
                    r.click()
                    time.sleep(2)
                    driver.back()
                    break

                except:
                    print("aaa")


# 쓰레드 갯수 지정
num_threads = 16
threads = []

# 쓰레드 돌리기
for _ in range(num_threads):
    thread = threading.Thread(target=open_webdriver)
    threads.append(thread)
    thread.start()

# 쓰레드 대기
for thread in threads:
    thread.join()
