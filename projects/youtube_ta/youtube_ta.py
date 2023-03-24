from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from io import BytesIO
from PIL import Image
import os
import time

def click_subtitles_button(driver):
    wait = WebDriverWait(driver, 10)
    subtitles_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ytp-subtitles-button")))
    subtitles_button.click()
    
def off_captions(driver):
    # # 스페이스바 누르기
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.SPACE)

    # c 누르기
    actions = ActionChains(driver)
    actions.send_keys('c')
    actions.perform()
    
driver_path = 'webdriver/chromedriver.exe'
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path=driver_path))
driver.maximize_window()

url = "https://www.youtube.com/watch?v=mkggXE5e2yk"
driver.get(url)

video_tag = driver.find_element(By.CSS_SELECTOR, 'video.html5-main-video')
print(video_tag.tag_name, video_tag.size, video_tag.location)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'video')))
location = video_tag.location
size = video_tag.size

start_button = driver.find_element(By.CSS_SELECTOR, '.ytp-large-play-button.ytp-button')
start_button.click()

off_captions(driver)

time.sleep(5)

file_dir = r"F:\Screenshots"
if not os.path.exists(file_dir):
    os.makedirs(file_dir)
count = 1
while True:
    screenshot = driver.get_screenshot_as_png()
    image = Image.open(BytesIO(screenshot))
    # image.show()

    # 왼쪽, 위쪽, 오른쪽, 아래쪽
    image = image.crop((110, 80, 110 + 1250, 80 + 700))
    
    filename = f"screenshot_{count}.png"
    temp = os.path.join(file_dir, filename)
    print(temp)
    image.save(temp)
    count += 1
    time.sleep(3)
    
driver.quit()
