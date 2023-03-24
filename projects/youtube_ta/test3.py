import cv2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
import numpy as np

# Chrome 드라이버 경로 설정
driver_path = 'Chrome 드라이버 경로'

# 웹 브라우저 열기
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()

# HTML 페이지 열기
driver.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

# 동영상 태그 찾기
video_tag = driver.find_element(By.CSS_SELECTOR, 'video.html5-main-video')

# 동영상 태그의 위치와 크기 구하기
location = video_tag.location
size = video_tag.size

# 모니터 화면 캡처
screenshot = driver.get_screenshot_as_png()

# 캡처한 이미지를 NumPy 배열로 변환
img = cv2.imdecode(np.frombuffer(screenshot, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

# 동영상 태그의 좌표 구하기
x = location['x']
y = location['y']
width = size['width']
height = size['height']

# 동영상 태그의 꼭짓점 좌표 구하기
top_left = (x, y)
top_right = (x + width, y)
bottom_left = (x, y + height)
bottom_right = (x + width, y + height)

# 동영상 태그 부분만 자르기
cropped_img = img[y:y+height, x:x+width]

# 자른 이미지 출력
with open('F:/test.png', 'wb') as f:
    buffered = BytesIO()
    cropped_img.save(buffered, format="PNG")
    f.write(buffered.getvalue())


# 웹 브라우저 닫기
driver.quit()
