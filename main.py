from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time


# 실행파일로 만들기
# pyinstaller --onefile main.py


# 유저 정보
user_info = ['학번', '아이디', '비밀번호']

# 로그인 박스 부분
input_boxes = {
    'std_id': '//*[@id="user.stu_nbr"]', 
    'id': '//*[@id="user.usr_id"]', 
    'pass': '//*[@id="user.passwd"]'
    }

# 각종 버튼들 
buttons = {
    'login': '//*[@id="loginForm"]/table/tbody/tr[4]/td/button[1]', 
    'end': '//*[@id="logout"]/button[1]',
    'submit': '',
    'test': '//*[@id="lectPackReqGrid_0"]/td[11]/a'
    }





def find_element(xpath):
    wait.until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return driver.find_element_by_xpath(xpath)

def login(boxes, value):

    std_id_box = find_element(boxes['std_id'])
    std_id_box.send_keys(value[0])

    id_box = find_element(boxes['id'])
    id_box.send_keys(value[1])

    pass_box = find_element(boxes['pass'])
    pass_box.send_keys(value[2])

    login_btn = find_element(buttons['login'])
    login_btn.click()

    driver.implicitly_wait(time_to_wait=10)
    print("Complete Login!")




if "__main__":

    start = time.time()

    user_info[0] = input("Student ID : ")
    user_info[1] = input("YES ID : ")
    user_info[2] = input("YES PW : ")
    row = input("row (0부터 시작) : ")

    major = '//*[@id="lectPackReqGrid_' + row + '"]/td[2]'
    total_possble = '//*[@id="lectPackReqGrid_' + row + '"]/td[8]'
    limit_std = '//*[@id="lectPackReqGrid_' + row + '"]/td[9]'
    buttons['submit'] = '//*[@id="lectPackReqGrid_' + row + '"]/td[11]/a'


    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    url = 'https://sugang.knu.ac.kr/'

    # # 쓸데없는 오류메세지 제거
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # browser = webdriver.Chrome(options=options)

    # # 오픈
    # browser.get(url)
    driver.get(url)
    alert = Alert(driver)       # 알람 제어


    driver.implicitly_wait(time_to_wait=10)
    time.sleep(1)
    # 팝업 닫기
    driver.switch_to_window(driver.window_handles[1])
    driver.close()
    driver.switch_to_window(driver.window_handles[0])

    # 페이지 로딩 대기
    driver.implicitly_wait(time_to_wait=10)


    login(input_boxes, user_info)

    mj_name = find_element(major).text
    total = find_element(total_possble).text

    while True:

        if time.time() - start >= 1000:         # 로그인 시간 초과 시 재 로그인
            
            end = find_element(buttons['end'])
            end.click()

            driver.implicitly_wait(time_to_wait=10)
            driver.switch_to_window(driver.window_handles[1])
            driver.close()
            driver.switch_to_window(driver.window_handles[0])
            driver.implicitly_wait(time_to_wait=10)
            print("Logout!")

            time.sleep(1)
            login(input_boxes, user_info)

            start = time.time()


        # 수강 제한 인원수 읽기
        std = find_element(limit_std)
        print('target :', mj_name, total, '/', std.text, int(time.time() - start), "sec...\t", end='\r')

        if int(std.text) != int(total):     # 신청 버튼 누르기
            print('Empty 1')
            submit = find_element(buttons['submit'])
            submit.click()

            time.sleep(1)
            alert.accept()

            end = find_element(buttons['end'])
            end.click()
            driver.implicitly_wait(time_to_wait=10)

            break
        else:               # 새로고침 하기
            driver.refresh()
            driver.implicitly_wait(time_to_wait=10)

    driver.close()
    print('complete')
