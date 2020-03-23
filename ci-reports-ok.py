# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
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
        print ('looking for APMMultiCanais')
        driver.find_element_by_id("area-issues").click()
      #  Select(driver.find_element_by_id("area-issues")).select_by_visible_text("APIMultiCanais")
      #  driver.find_element_by_id("application").click()
      #  print 'looking for api-monitor'
      #  Select(driver.find_element_by_id("application")).select_by_visible_text("api-monitor")
      #  print 'select api-monitor'
      #  driver.find_element_by_xpath("//table[@id='DataTables_Table_0']/thead/tr/th").click()
        print(driver.title)
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
