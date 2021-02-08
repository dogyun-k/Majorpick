from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time






user_info = ['2016115845', 'dudals5614', 'q1w1e1r1t1!']






driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
url = 'https://sugang.knu.ac.kr/'
driver.get(url)
alert = Alert(driver)       # 알람 제어


driver.implicitly_wait(time_to_wait=10)
# 팝업 닫기
driver.switch_to_window(driver.window_handles[1])
driver.close()
driver.switch_to_window(driver.window_handles[0])

# 페이지 로딩 대기
driver.implicitly_wait(time_to_wait=10)

input_boxes = {
    'std_id': '//*[@id="user.stu_nbr"]', 
    'id': '//*[@id="user.usr_id"]', 
    'pass': '//*[@id="user.passwd"]'
    }

buttons = {
    'login': '//*[@id="loginForm"]/table/tbody/tr[4]/td/button[1]', 
    'end': '//*[@id="logout"]/button[1]',
    'submit': '//*[@id="lectPackReqGrid_2"]/td[11]/a',
    'test': '//*[@id="lectPackReqGrid_0"]/td[11]/a'
    }

limit_std = '//*[@id="lectPackReqGrid_2"]/td[9]'




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





start = time.time()

login(input_boxes, user_info)

while True:

    if time.time() - start >= 1000:         # 로그인 시간 초과 시
        
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

    std = find_element(limit_std)

    print(std.text, int(time.time() - start))



    if std.text != '40':     # 신청 버튼 누르기

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