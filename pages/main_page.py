import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):
    url = 'https://xn----7sbb4ac0ad0be6cf.xn--p1ai/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

 # Locators
    category_tents = "//a[@data-cat-id='26']"
    category_trecking_tents = "//a[@href='/goods/trekking-tents/']"


# Getters
    def get_select_category_tents(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.category_tents)))

    def get_select_category_trekking_tents(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.category_trecking_tents)))



# Actions
    def click_select_category_tents(self):
        self.get_select_category_tents().click()
        print("click button select category tents")

    def click_select_category_trekking_tents(self):
        self.get_select_category_trekking_tents().click()
        print("click button select category trekking tents")


# Methods
    def select_category_tents(self):
        self.get_select_category_tents()
        self.click_select_category_tents()

    def select_category_trekking_tents(self):
        self.get_select_category_trekking_tents()
        self.click_select_category_trekking_tents()

    def start(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()

    # Method scroll to
    def scroll_to_trekking_tents(self):
        action = ActionChains(webdriver)
        t_shirt_red = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.category_trecking_tents)))
        action.move_to_element(t_shirt_red)








