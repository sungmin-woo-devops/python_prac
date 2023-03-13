import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoScreenshot():
    def demo_screen_captue(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.google.com")

        continuedemo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continuedemo.screenshot("/home/w/Workspace/python/test.png")
        continuedemo.click()
        time.sleep(2)
        driver.get_screenshot_as_file("/home/w/Workspace/python/test.png")
        driver.save_screenshot("/home/w/Workspace/python/test.png")

ddscreenshot = DemoScreenshot()
ddscreenshot.demo_screen_captue()
