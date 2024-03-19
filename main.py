# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image
from screenshot import screencapture

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options )
    driver.get("https://www.website.com")
    # try:
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "GTMDataLayerCode"))
    #     )
    #
    # finally:
    driver.save_screenshot('ss.png')
    pageSource = driver.page_source
    print(pageSource)
    driver.quit()

    #fileToWrite = open("page_source.html", "w")
    #fileToWrite.write(pageSource)
    #fileToWrite.close()
    #fileToRead = open("page_source.html", "r")
    #print(fileToRead.read())
    #fileToRead.close()
