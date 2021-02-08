from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
url = 'https://sugangpack.knu.ac.kr/'
driver.get(url)

# 페이지 로딩 대기
driver.implicitly_wait(time_to_wait=10)


wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="sugangSupportFront"]/div[3]/div[2]/table[1]/tbody/tr/td/font/text()[2]'))
)
sample = driver.find_elements_by_xpath('//*[@id="sugangSupportFront"]/div[3]/div[2]/table[1]/tbody/tr/td/font/text()[2]')

print(sample.text)


