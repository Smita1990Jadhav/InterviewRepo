#self.driver.find_element_by_id("country").send_keys("ind")
#self.driver.find_element_by_link_text("Indonesia").click()
#self.driver.find_element_by_class_name("checkbox-primary").click()
#self.driver.find_element_by_css_selector("input[type='submit']").click()
#success = self.driver.find_element_by_css_selector(".alert-success").text
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ConfirmPageC:
    def __init__(self, driver):
        self.driver = driver
    confirm = (By.ID, "country")
    confirm1 = (By.LINK_TEXT, "Indonesia")
    confirm2 = (By.CLASS_NAME, "checkbox-primary")
    confirm3 = (By.CSS_SELECTOR, "input[type='submit']")
    confirm4 = (By.CSS_SELECTOR, ".alert-success")

    #def ConfirmPageFun(self, phrase):
        #confirmS = self.driver.find_element(*ConfirmPageC.confirm)
        #confirmS.send_keys(phrase + Keys.RETURN)
    def ConfirmPageFun(self):
        return self.driver.find_element(*ConfirmPageC.confirm)

    def ConfirmPageFun1(self):
        return self.driver.find_element(*ConfirmPageC.confirm1)

    def ConfirmPageFun2(self):
        return self.driver.find_element(*ConfirmPageC.confirm2)

    def ConfirmPageFun3(self):
        return self.driver.find_element(*ConfirmPageC.confirm3)

    def ConfirmPageFun4(self):
        return self.driver.find_element(*ConfirmPageC.confirm4)



