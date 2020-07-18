
"""

Name : Vishal Bende

Task: Flipkard login and get personal information

Packages required to be installed: selenium

Note: Chromedriver file must be in same folder.

"""
import time
import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

CHROME_OPTIONS = Options()

# headless for open browser in background
#CHROME_OPTIONS.add_argument("--headless")

URL = 'https://www.flipkart.com/'

# current directory path
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DRIVER_PATH = os.path.join(BASE_PATH, 'chromedriver')

TIMEOUT = 100


class FlipKart:

    # constructor
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

        # open chrome and visit url
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=CHROME_OPTIONS)
        self.driver.implicitly_wait(30)
        self.driver.get(URL)

        # action object for mouse actions
        self.action = ActionChains(self.driver)

    def login(self):

        # send username and password
        self.driver.find_element_by_class_name("_2zrpKA").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(self.password)

        try:
            element = WebDriverWait(self.driver, TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='submit']/span"))
            )
            element.click()

        except:
            self.driver.quit()
            print('Page loading takes time !!')

        return True

    def go_to_profile(self):
        try:

            time.sleep(2)

            element = WebDriverWait(self.driver, TIMEOUT).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dHGf8H"))
            )

            profile_hower = self.action.move_to_element(element)
            profile_hower.perform()
            time.sleep(2)

            main_element = self.driver.find_element_by_class_name("dHGf8H")
            main_element.find_element_by_link_text('My Profile').click()

        except:
            self.driver.quit()
            print('Page loading takes time !!')



        return True

    def scrap_profile_information(self):
        time.sleep(4)

        first_name = self.driver.find_element_by_name("firstName").get_attribute('value')
        last_name = self.driver.find_element_by_name("lastName").get_attribute('value')
        email = self.driver.find_element_by_name("email").get_attribute('value')
        mobile = self.driver.find_element_by_name("mobileNumber").get_attribute('value')

        male = self.driver.find_element_by_id("Male")
        female = self.driver.find_element_by_id("Female")

        gender = ''
        gender = male.get_attribute('id') if male.is_selected() else gender
        gender = female.get_attribute('id') if female.is_selected() else gender

        response_dict = {
            "FirstName": first_name,
            "LastName": last_name,
            "Gender" : gender,
            "EmailId":email,
            "MobileNumber": mobile

        }

        self.driver.close()
        return response_dict


if __name__ == "__main__":

    # credentials
    username = '9404962673'
    password = 'reset123'

    user_info_list = list()

    flk = FlipKart(username, password)
    flk.login()
    flk.go_to_profile()

    response_data = flk.scrap_profile_information()

    user_info_list.append(response_data)

    print(user_info_list)







