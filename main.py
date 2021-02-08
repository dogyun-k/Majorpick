from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui as pg

std_id = pg.prompt(text='학번', title='수강대기', default='StudentID')
print(std_id)
web_id = pg.prompt(text='아이디', title='수강대기', default='ID')
print(web_id)
password = pg.password(text='비밀번호', title='수강대기', default='PW', mask='*')
print(password)

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
url = 'https://sugangpack.knu.ac.kr/'
driver.get(url)

# 페이지 로딩 대기
driver.implicitly_wait(time_to_wait=10)

input_boxes = {'std_id': '//*[@id="user.stu_nbr"]', 'id': '//*[@id="user.usr_id"]', 'pass': '//*[@id="user.passwd"]'}
buttons = {'login': '//*[@id="login"]/fieldset/ul[2]/li[1]/input'}


wait.until(
    EC.presence_of_element_located((By.XPATH, input_boxes['std_id']))
)
std_id_box = driver.find_element_by_xpath(input_boxes['std_id'])
std_id_box.send_keys(std_id)

wait.until(
    EC.presence_of_element_located((By.XPATH, input_boxes['id']))
)
id_box = driver.find_element_by_xpath(input_boxes['id'])
id_box.send_keys(web_id)

wait.until(
    EC.presence_of_element_located((By.XPATH, input_boxes['pass']))
)
pass_box = driver.find_element_by_xpath(input_boxes['pass'])
pass_box.send_keys(password)

wait.until(
    EC.presence_of_element_located((By.XPATH, buttons['login']))
)
login_btn = driver.find_element_by_xpath(buttons['login'])
# login_btn.click()


print(login_btn.text)