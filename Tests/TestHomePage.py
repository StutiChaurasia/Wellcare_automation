import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Locators.WellcareHomePageLocators import *
from Utilities.CommonUtilities import CommonUtil
from conftest import driver
from openpyxl import Workbook
from Utilities import Util
path = "C:\\Users\\stuti\\Downloads\\list.xlsx"
rows = Util.get_row_count(path, 'Sheet1')
data_list = []

class TestLoginPages:
    @pytest.mark.usefixtures("initiate_driver")
    def test_enter_city(self, initiate_driver):
        ca = CommonUtil()
        for k in range(2, 4):
            city_name = Util.read_data(path, "Sheet1", k, 2)
            city_code = Util.read_data(path, "Sheet1", k, 4)
            fill_data = city_name+" "+city_code+" USA"
            textbox = driver.find_element(by=By.XPATH, value=search_city_box)
            textbox.clear()
            textbox.send_keys(fill_data)
            time.sleep(2)
            textbox.send_keys(Keys.ENTER)
            time.sleep(5)
            driver.execute_script("window.scroll(0,100);")
            time.sleep(3)
            ca.click_element(search_all_available_plans)
            ca.click_element(search_type)
            ca.click_element(select_provider_type)
            searchbox = driver.find_element(by=By.XPATH, value=search_speciality)
            searchbox.send_keys("Internal")
            time.sleep(5)
            ca.click_element(select_internal_medicine)
            ca.click_element(select_internal_medicine)
            time.sleep(5)
            ca.click_element(search)
            time.sleep(10)
            driver.execute_script("window.scroll(0,document.body.scrollHeight);")
            time.sleep(10)
            no_of_results = driver.find_elements(by=By.XPATH, value='//webl-component[text() = "Show participating networks"]')
            for i in range(1,len(no_of_results)*2+1):
                j = str(i)
                list1 = []
                provider_name = "//ul[@class='list-unstyled search-results']/li["+j+"]/search-result/md-card/div/div/h2"
                provider_address = "//ul[@class='list-unstyled search-results']/li["+j+"]/search-result/md-card/div/div/p-standard-component[2]/span"
                provider_phone_no = "//ul[@class='list-unstyled search-results']/li["+j+"]/search-result/md-card/div/div/div/a"
                npi = "//ul//li["+j+"]//section[2][@role='tabpanel']//div[1]/div[11]/p[2]"
                show_details = "//*[@class='list-unstyled search-results']/li["+j+"]//div/button[2]/webl-component"
                location = "//div[@class='row wider-screen-container width-adjuster ng-scope']//ul/li["+j+"]/search-result/md-card//div/p-standard-component[1]/span"
                speciality = "//*[@class='list-unstyled search-results']/li["+j+"]//div[@class='row search-result-row']/div[1]/div[2]/span[1]"
                driver.execute_script("window.scroll(0,document.body.scrollHeight);")
                time.sleep(2)
                data = driver.find_element(By.XPATH, provider_name).text
                list1.append(data)
                data = driver.find_element(By.XPATH, provider_address).text
                list1.append(data)
                data = driver.find_element(By.XPATH, provider_phone_no).text
                list1.append(data)
                data = driver.find_element(By.XPATH, location).text
                list1.append(data)
                data = driver.find_element(By.XPATH, speciality).text
                list1.append(data)
                driver.execute_script("window.scroll(0,50);")
                time.sleep(2)
                ca.click_element(show_details)
                time.sleep(1)
                driver.execute_script("window.scroll(0,100);")
                data = driver.find_element(By.XPATH, npi).text
                list1.append(data)
                driver.execute_script("window.scroll(0,document.body.scrollHeight);")
                time.sleep(2)
                data_list.append(list1)
                wb = Workbook()
                ws = wb.active
                for d in data_list:
                    ws.append(d)
                wb.save("demoexcel.xlsx")
            driver.back()
            # time.sleep(2)
            driver.back()
            time.sleep(2)



















