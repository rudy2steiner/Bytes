from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    chrome_driver = '/Users/rudy/installment/chromedriver'
    login_url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9U6Ohtm&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
    driver = webdriver.Chrome(chrome_driver)
    wait = WebDriverWait(driver, 40)
    # driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(login_url)
    # assert "Python" in driver.title
    user_name = '淘金'
    passwd = 'xxxxxx'
    # time.sleep(5)
    # driver.find_element_by_xpath('//*[@id="module-YrEpAzATZ"]/div/div[1]/div[1]').click()
    # time.sleep(5)
    # driver.find_element_by_xpath('//*[@id="module-YrEpAzATZ"]/div/div[1]/div[2]').click()
    action_chains = ActionChains(driver)
    driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(user_name)
    driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(passwd)
    time.sleep(5)
    try:
        wait.until(EC.presence_of_element_located((By.ID, 'nc_1_n1t')))
         # if slider.is_displayed()
        # time.sleep(2)
        # html = BeautifulSoup(slider, 'lxml')
        # print(html)
        # d.click_and_hold(slider).click()
        slider = driver.find_element_by_xpath('//*[@id="nc_1_n1t"]')
        action_chains.drag_and_drop_by_offset(slider, xoffset=300, yoffset= 0).perform()
        time.sleep(0.5)
        wait.until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, 'div#nc_1__scale_text > span.nc-lang-cnt > b'), '验证通过'
        ))
        # action_chains.release().perform()
    except (NoSuchElementException, WebDriverException) as e:
        logger.error(e)
    driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
