import time

import allure
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Kong_3_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

 # Locators
    name_kong_3 = "//h1[@class='mt-1']"
    button_buy = "//button[@class='btn btn-lg btn-info ']"
    button_cart = "//a[@href='/cart/']"
    count_cart = "//b[@class='d-sm-inline d-none']"


# Getters
    def get_name_kong_3(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.name_kong_3)))

    def get_button_buy(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.button_buy)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))


# Actions
    def click_button_buy(self):
        self.get_button_buy().click()
        print("Click button buy")

    def click_button_cart(self):
        self.get_button_cart().click()
        print("Click button cart")


# Methods
    def assert_kong(self):
        with allure.step("Assert kong"):
            self.assert_word(self.get_name_kong_3(), "Палатка Splav «Kong 3»")
# сравнивает надпись с заданной





