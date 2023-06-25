import datetime
import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver


#  method get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url)

#  method assert word
    def assert_word(self, word, result):
        value_word = word.text
        print(value_word)
        assert value_word == result
        print("Good value word")

#  method screenshot
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Admin\\PycharmProjects\\pythonProjectHomeTask\\screen\\' + name_screenshot)


#  method assert URL

    def assert_url(self, result):
        with allure.step("assert_url"):
            get_url = self.driver.current_url
            print(get_url)
            assert get_url == result
            print("Good URL")

