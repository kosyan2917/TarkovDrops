import time

from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#tw-progress-bar-animation
class Drops:
    
    def __init__(self):
        options = webdriver.ChromeOptions()
        self.driver = uc.Chrome(executable_path='chromedriver.exe')
        with open('auth.txt', 'r') as f:
            try:
                self.login = f.readline()
                self.pw = f.readline()
            except Exception as err:
                print('Чекни текстовый файл')
                del self
    
    def mainloop(self):
        self.driver.get('https://www.twitch.tv/drops/inventory')
        login = self.driver.find_element_by_xpath(".//input[@id='login-username']")
        login.send_keys(self.login)
        pw = self.driver.find_element_by_xpath(".//input[@id='password-input']")
        pw.send_keys(self.pw)
        self.driver.find_element_by_xpath(".//div[@class='Layout-sc-nxg1ff-0 ibRTKs']").click()
        input('Тыкни че нить')
        while True:
                self.wait_until(".//div[@data-a-target='tw-progress-bar-animation']")
                el = self.driver.find_elements_by_xpath(".//div[text()='Получить сейчас']")
                print('Хожу по циклу')
                if el:
                    el[0].click()
                    print('Типа кликнул')
                    timesleep = 14000
                    print(f"Sleeping {timesleep} seconds")
                    time.sleep(timesleep)

                else:
                    elements = self.driver.find_elements_by_xpath(".//div[@data-a-target='tw-progress-bar-animation']")
                    for el in elements:
                        value = int(el.get_attribute('value'))
                        if value!=0:
                            timesleep = (1-value/100)*14400
                            print(f"Sleeping {timesleep} seconds")
                            time.sleep(timesleep)
                self.driver.refresh()
    
    def wait_until(self, xpath):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                         xpath)))
        
    def __del__(self):
        print('Бот самоуничтожился. Вероятно проблемы в auth.txt')
        
if __name__ == '__main__':
    drop_obj = Drops()
    drop_obj.mainloop()