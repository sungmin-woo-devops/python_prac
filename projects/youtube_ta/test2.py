from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
from PIL import Image
import os
from time import sleep

# Chrome 드라이버 경로 설정
driver_path = 'webdriver/chromedriver'

# YouTube 비디오 URL 설정
video_url = 'https://www.youtube.com/watch?v=owgBHMaByuo'

# 웹 브라우저 열기
driver = webdriver.Chrome(driver_path)
driver.maximize_window()

# YouTube 비디오 페이지 열기
driver.get(video_url)

# 비디오 재생까지 대기
sleep(5)

# 스크린샷 캡처 및 저장
for i in range(5):
# 스크린샷 캡처
    screenshot = driver.find_element(By.TAG_NAME, 'body')
    location = screenshot.location
    size = screenshot.size
    screenshot = driver.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    if left < 0:
        left = 0
    if top < 0:
        top = 0
    if right > screenshot.size[0]:
        right = screenshot.size[0]
    if bottom > screenshot.size[1]:
        bottom = screenshot.size[1]
    screenshot = screenshot.crop((left, top, right, bottom))
    screenshot.save(f'screenshot_{i+1}.png')

    
    # 시간 지연
    sleep(10)

# 웹 브라우저 닫기
driver.quit()
