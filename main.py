from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time






user_info = ['2016116256', 'kdk124578', 'kdk519437!']

# 수강과목 제한수 
limit_std_num = 40





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

    'submit': '//*[@id="lectPackReqGrid_2"]/td[11]/a',      # <<< 해당 수강과목 신청버튼 XPath 복사해서 넣어야함.

    'test': '//*[@id="lectPackReqGrid_0"]/td[11]/a'
    }


limit_std = '//*[@id="lectPackReqGrid_2"]/td[9]'            # <<< 해당 수강과목 제한수 XPath 복사해서 넣어야함.




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
    print(std.text, int(time.time() - start))

    if int(std.text) % 10 != 0:     # 신청 버튼 누르기
                                    # 해당 수식은 수강신청 과목 제한 수가 10으로 나눠떨어진다고 가정함.

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