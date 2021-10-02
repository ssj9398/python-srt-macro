import time
import telegram
from selenium import webdriver
#from bs4 import BeautifulSoup


driver = webdriver.Chrome('C:/Users/aclie/Downloads/chromedriver_win32/chromedriver.exe')

url = 'https://etk.srail.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000'
driver.get(url)
id = '???'
pw = '???'

driver.find_element_by_xpath("//input[@id='srchDvNm01']").send_keys(id)
driver.find_element_by_xpath("//input[@id='hmpgPwdCphd01']").send_keys(pw)
driver.find_element_by_xpath("//input[@value='확인']").click()

# time.sleep(0.1)

driver.switch_to_window(driver.window_handles[0])

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
    time.sleep(0.2)
    driver.execute_script("window.scrollTo(0, 0)")
    driver.get(url2)
    start = '수서'
    end = '부산'

    driver.find_element_by_xpath("//input[@id='dptRsStnCdNm']").clear()
    driver.find_element_by_xpath("//input[@id='arvRsStnCdNm']").clear()

    driver.find_element_by_xpath("//input[@id='dptRsStnCdNm']").send_keys(start)
    driver.find_element_by_xpath("//input[@id='arvRsStnCdNm']").send_keys(end)
    driver.find_element_by_xpath("//input[@value='조회하기']").click()

    reservation = driver.find_elements_by_link_text('예약하기')

    search_reservation = driver.find_elements_by_css_selector("div.tbl_wrap.th_thead > table > tbody > tr> td > a")
    for r in search_reservation:
        print(r.text)
        if r.text =='예약하기':
            print("빈좌석 발견 예약을 시작합니다 특실일 경우 패스")
            r.click()

            time.sleep(1)
            startsrt = driver.find_elements_by_css_selector("#list-form > fieldset > div:nth-child(4) > table > tbody > tr > td.dptTm")
            for i in startsrt:
                print(i.text)
                bot = telegram.Bot(token='???')
                bot.send_message(chat_id=???, text=i.text+"분 기차가 예약되었습니다 결제하세요")
                driver.back()
            break




            # print("예약할거 찾기 성공")
            # aa = driver.find_elements_by_xpath("//*[@id='result-form']/fieldset/div/table/tbody/tr/td/a/span")
            #
            # for a in aa:
            #     if a.text =='예약하기':
                    # print(soup.html)
                    # print("listsize : "+len(aa))
                    # print("aaaaa"+aa.parent)
                    # print("aaaaa"+a.text)
            # test.find_element_by_xpath("//a[@button]").click()
    # print(test)

    # for test in reservation:
    #     print(test.text)
    # a = driver.find_element_by_xpath("//a[@class='btn_burgundy_dark']")
    # for test in a:
    #     print(test.text)
    # time.sleep(1)
    # driver.execute_script("window.scrollTo(0, 0)")
    # driver.find_element_by_xpath("//input[@value='조회하기']").click()








# while True:
#     time.sleep(1)
#     driver.refresh()
#     time.sleep(2)
#     for i in range(3):
#         notReadEmail = driver.find_elements_by_xpath("//a[@style='font-weight: bold;']")
#         print(driver.find_elements_by_xpath("//a[@style='font-weight: bold;']"))
#         for title in notReadEmail:
#             print(title.text)
#             bot = telegram.Bot(token='2003347573:AAGwG9bppqE2HkM4LCmfqRzZk6otPvc0gIo')
#             bot.send_message(chat_id=2029589225, text="`"+title.text)
