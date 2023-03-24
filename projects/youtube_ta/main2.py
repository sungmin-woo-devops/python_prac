from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
from time import sleep
from PIL import Image

# Selenium webdriver 설정
# chromedriver 경로 지정
driver_path = 'webdriver/chromedriver'

# webdriver 객체 생성
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path=driver_path))

# 유튜브 강의 URL 설정
url = "https://www.youtube.com/watch?v=fy8SHvNZGeE"

# 브라우저를 열고 URL 로 이동
driver.get(url)

# 유튜브 동영상의 비디오 태그 가져오기
video_tag = driver.find_element(By.CSS_SELECTOR, '.video-stream.html5-main-video')

# 비디오 태그가 로딩될 때까지 대기
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'video')))

# 비디오 영역의 크기 가져오기
location = video_tag.location
size = video_tag.size

# 스크린샷 찍기
screenshot = driver.get_screenshot_as_png()

# 이미지 데이터를 PIL 이미지 객체로 변환
image = Image.open(BytesIO(screenshot))
image = image.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))

# 스크린샷 이미지 저장하기
filepath = "F:\Screenshots"
count = 1
while True:
    sleep(10)
    filename = f"screenshot_{count}.png"
    temp = f"{filepath}\{filename}"
    print(temp)
    image.save(temp)
    count += 1
