from selenium import webdriver
import time
class Login:
    txt_Company_id="Company"
    txt_Username_id="Username"
    txt_Password_id="password-field"
    btn_Login_id="login-button"
    def __init__(self,driver):
        self.driver=driver
    def setCompany(self,companyName):
        self.driver.find_element_by_id(self.txt_Company_id).clear()
        time.sleep(2)
        self.driver.find_element_by_id(self.txt_Company_id).send_keys(companyName)
    def setUsername(self,username):
        self.driver.find_element_by_id(self.txt_Username_id).clear()
        time.sleep(2)
        self.driver.find_element_by_id(self.txt_Username_id).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element_by_id(self.txt_Password_id).clear()
        time.sleep(2)
        self.driver.find_element_by_id(self.txt_Password_id).send_keys(password)
    def clickLogin(self):
        self.driver.find_element_by_id(self.btn_Login_id).click()