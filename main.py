import time
from telnetlib import EC

import telegram
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('E:/잡동사니/crome/chromedriver.exe')

url = 'https://etk.srail.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000'
driver.get(url)
id = ''
pw = ''

driver.find_element_by_xpath("//input[@id='srchDvNm01']").send_keys(id)
driver.find_element_by_xpath("//input[@id='hmpgPwdCphd01']").send_keys(pw)
driver.find_element_by_xpath("//input[@value='확인']").click()

time.sleep(0.1)

# driver.switch_to_window(driver.window_handles[1])

url2 = 'https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000'
driver.get(url2)




# start = '수서'
# end = '대전'
#
# driver.find_element_by_xpath("//input[@id='dptRsStnCdNm']").clear()
# driver.find_element_by_xpath("//input[@id='arvRsStnCdNm']").clear()
#
# driver.find_element_by_xpath("//input[@id='dptRsStnCdNm']").send_keys(start)
# driver.find_element_by_xpath("//input[@id='arvRsStnCdNm']").send_keys(end)
# driver.find_element_by_xpath("//input[@value='조회하기']").click()

while True:
  #  time.sleep(0.2)
    #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "idname")))
    driver.execute_script("window.scrollTo(0, 0)")
    driver.get(url2)
    start = '수서'
    end = '동대구'

    #날짜선택
    driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/div[1]/div/div/div[3]/div[1]/a').click()
    driver.find_element_by_xpath('//*[@id="ui-id-9"]').click()

    #시간선택
    driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/div[1]/div/div/div[3]/div[2]/a').click()
    driver.find_element_by_xpath('//*[@id="ui-id-78"]').click()

    # 출발지 도착지 지정
    driver.find_element_by_xpath("//input[@id='dptRsStnCdNm']").clear()
    driver.find_element_by_xpath("//input[@id='arvRsStnCdNm']").clear()
    driver.find_element_by_xpath("//input[@id='dptRsStnCdNm']").send_keys(start)
    driver.find_element_by_xpath("//input[@id='arvRsStnCdNm']").send_keys(end)

    #조회하기 클릭
    driver.find_element_by_xpath("//input[@value='조회하기']").click()

    reservation = driver.find_elements_by_link_text('예약하기')

    search_reservation = driver.find_elements_by_css_selector("div.tbl_wrap.th_thead > table > tbody > tr> td > a")
    for r in search_reservation:
        print(r.text)
        if r.text =='예약하기':
            print("빈좌석 발견 예약을 시작합니다 특실일 경우 패스")
            r.click()
            #wait = WebDriverWait(driver, 10)
            #element = wait.until(EC.element_to_be_clickable((By.XPATH, "#list-form > fieldset > div:nth-child(4) > table > tbody > tr > td.dptTm")))
            time.sleep(1)
            startsrt = driver.find_elements_by_css_selector("#list-form > fieldset > div:nth-child(4) > table > tbody > tr > td.dptTm")
            for i in startsrt:
                print(i.text)
                bot = telegram.Bot(token='')
              #  bot.send_message(chat_id=2029589225, text=i.text+"분 기차가 예약되었습니다 결제하세요")
                driver.back()
            break

