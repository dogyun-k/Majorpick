from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import pyautogui

# std_id = pg.prompt(text='학번', title='수강대기', default='StudentID')
# web_id = pg.prompt(text='아이디', title='수강대기', default='ID')
# password = pg.password(text='비밀번호', title='수강대기', default='PW', mask='*')

user_info = ['2016116256', 'kdk124578', 'kdk519437!']

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
url = 'https://sugang.knu.ac.kr/'
driver.get(url)

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
    'submit': '//*[@id="lectPackReqGrid_1"]/td[11]/a'
    }

limit_time = '//*[@id="timeStatus"]'
limit_std = '//*[@id="lectPackReqGrid_1"]/td[9]'



def login(boxes, value):

    wait.until(
        EC.presence_of_element_located((By.XPATH, boxes['std_id']))
    )
    std_id_box = driver.find_element_by_xpath(boxes['std_id'])
    std_id_box.send_keys(value[0])

    wait.until(
        EC.presence_of_element_located((By.XPATH, boxes['id']))
    )
    id_box = driver.find_element_by_xpath(boxes['id'])
    id_box.send_keys(value[1])

    wait.until(
        EC.presence_of_element_located((By.XPATH, boxes['pass']))
    )
    pass_box = driver.find_element_by_xpath(boxes['pass'])
    pass_box.send_keys(value[2])

    wait.until(
        EC.presence_of_element_located((By.XPATH, buttons['login']))
    )
    login_btn = driver.find_element_by_xpath(buttons['login'])
    login_btn.click()





login(input_boxes, user_info)

driver.implicitly_wait(time_to_wait=10)
wait.until(
    EC.presence_of_element_located((By.XPATH), limit_std)
)
temp = driver.find_element_by_xpath(limit_std)
print('123')