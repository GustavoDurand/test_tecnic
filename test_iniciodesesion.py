import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestIniciodesesion():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_iniciodesesion(self):
    self.driver.get("https://simple.ripley.cl/")
    self.driver.set_window_size(1200, 772)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".my-account__box")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, ".my-account__box").click()
    self.driver.find_element(By.CSS_SELECTOR, "div > .my-account__desktop:nth-child(2)").click()
    self.driver.find_element(By.NAME, "ws_username").click()
    self.driver.find_element(By.NAME, "ws_username").send_keys("")
    self.driver.find_element(By.NAME, "password").send_keys("")
    self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".svg-icon-ripley_com > use")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, "strong")
    assert len(elements) > 0
  
