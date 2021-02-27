
#products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
#self.driver.find_element_by_css_selector(".btn-primary").click()
#self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
#productname = product.find_element_by_xpath("div/h4/a").text
from selenium.webdriver.common.by import By

from PageObject.ConfirmPage import ConfirmPageC


class CheckoutPageC:

    def __init__(self, driver):
        self.driver = driver
    check = (By.XPATH, "//div[@class='card h-100']")
    check1 = (By.CSS_SELECTOR, ".btn-primary")
    check2 = (By.XPATH, "//button[@class='btn btn-success']")





    def CheckoutPageFun(self):
        return self.driver.find_elements(*CheckoutPageC.check)

    def CheckoutPageFun1(self):
        return self.driver.find_element(*CheckoutPageC.check1)

    def CheckoutPageFun2(self):
        return self.driver.find_element(*CheckoutPageC.check2)
        """
        self.driver.find_element(*CheckoutPageC.check2).click()
        ConfirmPageV = ConfirmPageC(self.driver)
        return ConfirmPageV
         """

