from selenium.webdriver.common.by import By

from PageObject.CheckoutPage import CheckoutPageC


class HomePageC:

    def __init__(self, driver):
        self.driver = driver
    #self.driver.find_element_by_xpath("//a[text()='Shop']").click()
    shop = (By.XPATH, "//a[text()='Shop']")
    name = (By.NAME, "name")
    #driver.find_element_by_name("name").send_keys("Smita")
    email = (By.NAME, "email")
    #driver.find_element_by_name("email").send_keys("jadhavpiya1990@gmail.com")
    password = (By.ID, "exampleInputPassword1")
    #driver.find_element_by_id("exampleInputPassword1").send_keys("Piya@123")
    checkbox = (By.ID, "exampleCheck1")
    #driver.find_element_by_id("exampleCheck1").click()
    getgender = (By.ID, "exampleFormControlSelect1")
    #obj = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
    radiob = (By.ID, "inlineRadio2")
    #driver.find_element_by_id("inlineRadio2").click()
    submit = (By.XPATH, "//input[@value='Submit']")
    #driver.find_element_by_xpath("//input[@value='Submit']").click()
    successmsg = (By.CSS_SELECTOR, "[class*='alert-success']")
    #AlertText = driver.find_element_by_css_selector("[class*='alert-success']").text

    def HomePageFun(self):
        return self.driver.find_element(*HomePageC.shop)
    def getname(self):
        return self.driver.find_element(*HomePageC.name)
    def getemail(self):
        return self.driver.find_element(*HomePageC.email)
    def getpassword(self):
        return self.driver.find_element(*HomePageC.password)
    def checkboxopt(self):
        return self.driver.find_element(*HomePageC.checkbox)
    def dropdn(self):
        return self.driver.find_element(*HomePageC.getgender)
    def radiobopt(self):
        return self.driver.find_element(*HomePageC.radiob)
    def submitb(self):
        return self.driver.find_element(*HomePageC.submit)
    def successmsgfun(self):
        return self.driver.find_element(*HomePageC.successmsg)

        """self.driver.find_element(*HomePageC.shop).click()
        CheckoutPageV = CheckoutPageC(self.driver)
        return CheckoutPageV"""
