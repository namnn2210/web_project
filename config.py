import yaml
from selenium import webdriver


class Config(object):
    def __init__(self):
        with open('base_config.yaml') as file:
            cfg = yaml.load(file, Loader=yaml.FullLoader)
        driver_path = cfg.get('driver').get('path')
        self.driver = webdriver.Chrome(driver_path)
        self.target_page = cfg.get('target_page').get('url')

    def get_driver(self):
        return self.driver

    def get_target_page(self):
        return self.target_page
