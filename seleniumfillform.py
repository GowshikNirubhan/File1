from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
 
class Suman:
    driver = webdriver.Chrome()

     
    def fill_form(self,url):
        # Get the Data
        email = "niru@example.com"
        password = "123456"
 
        # Get the XPATH / ID / Class
        
        email_xpath = "/html/body/form/input[1]"
        password_path = "/html/body/form/input[2]"
        submit_button_xpath = "/html/body/form/button"
        try:
            # open the webpage
            self.driver.get(url)
 
            #find the XPATH of the HTML element present on the webpage
            
            email_xpath=self.driver.find_element(by=By.XPATH, value=email_xpath)
            password_xpath=self.driver.find_elemet(by=By.XPATH, value=password_path)
            submit_button_xpath=self.driver.find_element(by=By.XPATH, value=submit_button_xpath)
 
            # fill the HTML form
           
            email_xpath.send_keys(email)
            password_xpath.send_keys(password)
            time.sleep(10)
 
            # click on the Submit button
            submit_button_xpath.click()
        except:
            print("ERROR : XPATH not found !")
s = Suman()            
url = "http://127.0.0.1:5500/xpath.html"
s.fill_form(url)


