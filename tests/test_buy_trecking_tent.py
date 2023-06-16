import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.cart_page import Cart_page
from pages.kong_3_page import Kong_3_page
from pages.main_page import Main_page
from pages.trekking_tents_page import Trakking_tents_page


def test_buy_trecking_tent():

        driver = webdriver.Chrome()
        print("start smoke test")

        st = Main_page(driver)
        st.start()

        mp = Main_page(driver)
        mp.select_category_tents()

        # driver.execute_script("window.scroll(0,270)")
        scrl = Main_page(driver)
        scrl.scroll_to_trekking_tents()

        mp_2 = Main_page(driver)
        mp_2.select_category_trekking_tents()

        cbs = Trakking_tents_page(driver)
        cbs.click_checkbox_splav()

        ck_3 = Trakking_tents_page(driver)
        ck_3.click_kong_3()

        aw = Kong_3_page(driver)
        aw.assert_kong()

        ckb = Kong_3_page(driver)
        ckb.click_button_buy()
        time.sleep(3)

        ckbc = Kong_3_page(driver)
        ckbc.click_button_cart()

        asurl = Base(driver)
        asurl.assert_url("https://xn----7sbb4ac0ad0be6cf.xn--p1ai/login/")

        log = Cart_page(driver)
        log.login_connection()

        time.sleep(10)





        print("Finish smoke test")
        driver.quit()