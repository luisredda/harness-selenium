# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest, time, re, os



class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(60)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        url = os.environ['TESTURL']
        driver = self.driver
        print('opening ci-reports page')
        driver.get(url)
        delay = 30 
        try:
            print ('looking for Area Issues')
            driver.find_element_by_id("area-issues").click()
            print ('looking for APMMultiCanais')
            Select(driver.find_element_by_id("area-issues")).select_by_visible_text("APIMultiCanais")
            print ('looking for application')
            myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'application')))
            driver.find_element_by_id("application").click()
            print ('looking for api-monitor')
            Select(driver.find_element_by_id("application")).select_by_visible_text("api-monitor")
            print ('looking for table')
            driver.find_element_by_xpath("//table[@id='DataTables_Table_0']/thead/tr/th").click()
            print(driver.title)
        except TimeoutException:
            print "Loading took too much time!"
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
