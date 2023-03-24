from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
from PIL import Image
import os
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from youtube_ta import driver

def off_captions(driver):
    wait = WebDriverWait(driver, 10)
    video = wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))
    action = ActionChains(driver).move_to_element(video)
    action.perform()
    settings = driver.find_element(By.CSS_SELECTOR, ".ytp-settings-button")
    settings.click()
    captions = driver.find_element(By.XPATH, "//div[contains(text(),'Subtitles/CC')]")
    captions.click()
    off = driver.find_element(By.XPATH, "//div[contains(text(),'Off')]")
    off.click()