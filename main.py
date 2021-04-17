# Python 3.8, Selenium 3.141.0
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

PATH = "chromedriver_win32/chromedriver.exe"
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"
driver = webdriver.Chrome(desired_capabilities=caps, executable_path=PATH)


def run():
    driver.get('https://ppt.mfa.gov.cn/appo/index.html')
    print(driver.title)
    time.sleep(1)

    buttons = driver.find_elements(By.XPATH, '//button')
    buttons[13].click()
    time.sleep(1)

    reservation_link = driver.find_element_by_id('startReservation')
    reservation_link.click()

    checkbox = driver.find_element_by_id('agree')
    checkbox.click()

    next_step_button = driver.find_element_by_id('myButton')
    next_step_button.click()

    time.sleep(2)

    driver.quit()


if __name__ == '__main__':
    run()

