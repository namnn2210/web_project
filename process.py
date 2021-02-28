from config import Config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
import time
cfg = Config()


def do_process():
    driver = cfg.get_driver()
    page = cfg.get_target_page()
    driver.get(page)
    logger.info('Start window title: %s' % driver.title)
    try:
        gg_login_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "mod-third-party-login-google"))
        )
        gg_login_btn.click()
        logger.info('Google login btn position: %s' % gg_login_btn)
        logger.info('Windows: %s' % driver.window_handles)
        gg_login_window = driver.window_handles[1]
        driver.switch_to_window(gg_login_window)
        logger.info('Login window title: %s' % driver.title)
        logger.info('Login window title: %s' % driver.find_element_by_class_name('Xb9hP'))
        email_input = driver.find_element_by_xpath("//input[@id='identifierId']")
        email_input.send_keys('temperaturelimitation5028@gmail.com')
        email_input.send_keys(Keys.RETURN)
        # try:
        #     email_div = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "Xb9hP")))
        #     logger.info('Email div: %s' % email_div)
        #     email_input = email_div.find_element(By.ID("identifierId"))
        #     email_input.send_keys('temperaturelimitation5028@gmail.com')
        #     email_input.send_keys(Keys.RETURN)
        # except Exception as ex:
        #     logger.info('Error %s' % str(ex))
        time.sleep(30)
        # results_list = result_div.find_element_by_class_name('shopee-search-item-result__items')
        # results = results_list.find_elements_by_class_name('shopee-search-item-result__item')
        # for result in results:
        #     try:
        #         a = result.find_element_by_tag_name('a')
        #         logger.info(a.text)
        #     except Exception as ex:
        #         logger.info('Error %s' % result)
    finally:
        driver.quit()
