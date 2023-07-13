import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Trakking_tents_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

 # Locators
    checkbox_splav = "//input[@class='debug filter-50']"
    kong_3 = "//a[@href='/goods/trekking-tents/125550-palatka-splav-kong-3.html']"



# Getters
    def get_checkbox_splav(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_splav)))

    def get_kong_3(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.kong_3)))



# Actions
    def click_checkbox_splav(self):
        self.get_checkbox_splav().click()
        print("Click checkbox splav")

    def click_kong_3(self):
        self.get_kong_3().click()
        print("Click kong 3")


# Methods
    def select_checkbox_splav(self):
        with allure.step("Select checkbox splav"):
            self.get_checkbox_splav()
            self.click_checkbox_splav()

    def select_kong_3(self):
        with allure.step("Select kong_3"):
            self.get_kong_3()
            self.click_kong_3()




