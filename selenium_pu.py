from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import logging
import json
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def selenium_pu(driver, page_url):
    driver.get(page_url)
    page_result = {}
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'imageList'))
        )
        page_result['title'] = driver.title
        #driver.find_element_by_tag_name()
        images = driver.find_element_by_class_name('imageList').find_elements_by_tag_name('a')
        imgs = []
        for a in images:
            print(a.get_attribute('href'))
            print(a.get_attribute('title'))
            imgs.append({'href': a.get_attribute('href'), 'title': a.get_attribute('title')})
        page_result['qu'] = imgs
    finally:
        time.sleep(0.2)
    return page_result


if __name__ == "__main__":
    chrome_driver = '/Users/rudy/installment/chromedriver'
    driver = webdriver.Chrome(chrome_driver)
    try:
        page = selenium_pu(driver, 'http://www.qupu123.com/puyou/shangchuan/p336321.html')
        print(json.dumps(page))
    finally:
        driver.quit()