from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from config.configdata import explicit_wait_time
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC


class CommonUtil:
    def get_element_text(self, element):
        WebDriverWait(driver, explicit_wait_time).until(
            EC.visibility_of_element_located((By.XPATH, element)))
        text = driver.find_element(by=By.XPATH, value=element)
        return text

    def click_element(self, element):
        WebDriverWait(driver, explicit_wait_time).until(
            EC.element_to_be_clickable((By.XPATH, element)))
        driver.find_element(by=By.XPATH, value=element).click()
