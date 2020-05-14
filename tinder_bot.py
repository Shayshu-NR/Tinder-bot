from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep



#Python bot class
class webBot():
    def __init__(self):
        self.driver = webdriver.Chrome('C:/bin/chromedriver.exe')

    def login(self):
        self.driver.get("https://tinder.com/")

        sleep(5)

        #Check if the "more options" element exists
        # more_options = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
        # more_options.click()
        # sleep(1)

        connect_fb = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        connect_fb.click()


        base_window = self.driver.window_handles[0]
        pop_up_window = self.driver.window_handles[1]

        self.driver.switch_to_window(pop_up_window)

        fb_email = self.driver.find_element_by_xpath('//*[@id="email"]') 
        fb_email.send_keys('1234567890')
        fb_pass = self.driver.find_element_by_xpath('//*[@id="pass"]')
        fb_pass.send_keys('password')
        fb_login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        fb_login.click()

        sleep(5)

        self.driver.switch_to_window(base_window)

        allow_location = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        allow_location.click()
        not_intrest = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        not_intrest.click()
   

    
    



