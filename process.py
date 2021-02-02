from config import Config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger

cfg = Config()


def do_process():
    driver = cfg.get_driver()
    page = cfg.get_target_page()
    driver.get(page)
    search_bar = driver.find_element_by_class_name('shopee-searchbar-input__input')
    search_bar.send_keys('ốp iphone')
    search_bar.send_keys(Keys.RETURN)
    try:
        result_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopee-search-item-result"))
        )
        results_list = result_div.find_element_by_class_name('shopee-search-item-result__items')
        results = results_list.find_elements_by_class_name('shopee-search-item-result__item')
        for result in results:
            try:
                a = result.find_element_by_tag_name('a')
                logger.info(a.text)
            except Exception as ex:
                logger.info('Error %s' % result)
    finally:
        driver.quit()
