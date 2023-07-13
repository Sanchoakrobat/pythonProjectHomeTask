import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Cart_page(Base):


 # Locators
    id_phone = "//input[@id='id_phone']"
    id_email = "//input[@id='id_email']"
    next_btn = "//input[@id='next_btn']"
    id_password = "//input[@id='id_password']"
    id_delivery_type_1 = "//input[@id='id_delivery_type_1']"
    id_name = "//input[@id='id_name']"
    id_zip_code = "//input[@id='id_zip_code']"
    id_address = "//textarea[@id='id_address']"
    checkbox_comment = "//label[@for='id_m-5']"


# Getters
    def get_id_phone(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.id_phone)))
    # обращается к локатору телефон

    def get_id_email(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.id_email)))
    # обращается к локатору имейл

    def get_next_btn(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.next_btn)))

    def get_id_password(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.id_password)))

    def get_id_delivery_type_1(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.id_delivery_type_1)))

    def get_id_name(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.id_name)))

    def get_id_zip_code(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.id_zip_code)))

    def get_id_address(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.id_address)))

    def get_checkbox_comment(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_comment)))


# Actions
    def input_id_phone(self, id_phone):
        self.get_id_phone().send_keys(id_phone)
        print("Input phone")

    def input_id_email(self, id_email):
        self.get_id_email().send_keys(id_email)
        print("Input email")

    def input_id_password(self, id_password):
        self.get_id_password().send_keys(id_password)
        print("Input password")


    def click_next_btn(self):
        self.get_next_btn().click()
        print("Click button next")

    def click_checkbox_id_delivery_type_1(self):
        self.get_id_delivery_type_1().click()
        print("Click delivery type 1 == Доставка Почтой России (от 300 руб.)")

    def input_id_name(self, id_name):
        self.get_id_name().send_keys(id_name)
        print("Input name")

    def input_id_zip_code(self, id_zip_code):
        self.get_id_zip_code().send_keys(id_zip_code)
        print("Input zip_code")

    def input_id_address(self, id_address):
        self.get_id_address().send_keys(id_address)
        print("Input address")

    def click_checkbox_comment(self):
        self.get_checkbox_comment().click()
        print("Click checkbox comment == Спасибо, вы клёвые ^_^")


# Methods
    def login_connection(self):
        with allure.step("login_connection"):
            self.input_id_phone("+9999999999")
            self.input_id_email("kashin.alexandr.vasilevich@gmail.com")
            self.click_next_btn()
            self.input_id_password("QjnfmzVQ")
            self.click_next_btn()
            self.click_checkbox_id_delivery_type_1()
            self.click_next_btn()
            self.input_id_name("Ivan Ivanov")
            self.input_id_zip_code("610000")
            self.input_id_address("Петровка 38")
            self.click_next_btn()
            self.click_checkbox_comment()
            self.get_screenshot()
        # вводит все необходимые данные для отправки товара



