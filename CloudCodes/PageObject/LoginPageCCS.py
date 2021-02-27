from selenium.webdriver.common.by import By

class LoginPageCCS1:

    def __init__(self, driver):
        self.driver = driver

    name = (By.ID, "login-name")
    clickbt=(By.CSS_SELECTOR, "signinbtn")
    password = (By.NAME, "password")
    getpsw= (By.XPATH,"//input[@type='submit']")
    announce =(By.ID, "announcemntFooterbtn")



    def get_loginname(self):
        return self.driver.find_element(*LoginPageCCS1.name)
    def checkbtn(self):
        return self.driver.find_element(*LoginPageCCS1.clickbt)
    def password1(self):
        return self.driver.find_element(*LoginPageCCS1.password)
    def getpassword1(self):
        return self.driver.find_element(*LoginPageCCS1.getpsw)
    def announceid(self):
        return self.driver.find_element(*LoginPageCCS1.announce)