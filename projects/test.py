from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=fy8SHvNZGeE")

play_button = driver.find_element(By.CSS_SELECTOR, '.ytp-play-button')
play_button.click()

driver.save_screenshot('F:\screenshot.png')
driver.quit()