from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
from PIL import Image

# webdriver 설정 (Chrome, Firefox 등)
driver_path = 'webdriver/chromedriver'
browser = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path=driver_path))

# 브라우저 사이즈
browser.set_window_size(1200, 800)

# 페이지 이동
browser.get("https://www.youtube.com/watch?v=TNpu16eFvJ0")

# 비디오 영역의 태그 요소 가져오기
video_tag = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "video")))
print(video_tag.tag_name)

# 비디오 영역의 위치와 크기 가져오기
location = video_tag.location
size = video_tag.size

# 스크린샷 찍기
screenshot = browser.get_screenshot_as_png()

# PIL 라이브러리의 Image 모듈을 이용해 스크린샷 이미지를 메모리에 올리기
image = Image.open(BytesIO(screenshot))

print(location, size)

# PIL 라이브러리의 crop() 메소드를 이용해 비디오 영역만 잘라내기
# image = image.crop((0,0,735,413))
image = image.crop((location['x'], location['y'], location['x'] + size['width'] + 500, location['y'] + size['height'] + 500))
#image = image.crop((31, 30, 800, 531))
# 캡처한 이미지 저장하기
image.save("F:/a.png")

# 브라우저 종료
browser.quit()
