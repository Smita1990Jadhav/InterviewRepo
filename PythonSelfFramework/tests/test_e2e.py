#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#import pytest
from PageObject.CheckoutPage import CheckoutPageC
from PageObject.ConfirmPage import ConfirmPageC
from PageObject.HomePage import HomePageC
from utilities.BaseClass import BaseClass1
#@pytest.mark.usefixtures("setup")
#phrase = "ind"



class TestOne(BaseClass1):


    def test_e2e(self):


        HomepageV = HomePageC(self.driver)
        HomepageV.HomePageFun().click()
        #self.driver.find_element_by_xpath("//a[text()='Shop']").click()
        CheckoutPageV = CheckoutPageC(self.driver)
        #CheckoutPageV = CheckoutPageV.CheckoutPageFun()
        products = CheckoutPageV.CheckoutPageFun()


        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        for product in products:

            productname = product.find_element_by_xpath("div/h4/a").text

            if productname == "Blackberry":

                product.find_element_by_xpath("div/button").click()

        #CheckoutPageV1 = CheckoutPageC(self.driver)
        CheckoutPageV.CheckoutPageFun1().click()
        #self.driver.find_element_by_css_selector(".btn-primary").click()

        #CheckoutPageV2 = CheckoutPageC(self.driver)
        CheckoutPageV.CheckoutPageFun2().click()
        #ConfirmPageV = CheckoutPageV.CheckoutPageFun2()
        #ConfirmPageV.CheckoutPageFun2().click()
        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

        ConfirmPageV = ConfirmPageC(self.driver)
        ConfirmPageV.ConfirmPageFun().send_keys("Ind")
        #ConfirmPageV.ConfirmPageFun(phrase)
        #ConfirmPageV = CheckoutPageV.ConfirmPageFun(phrase)
        #self.driver.find_element_by_id("country").send_keys("ind")

        #wait = WebDriverWait(self.driver, 7)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Indonesia")))
        self.VerifyText("Indonesia")
        #ConfirmPageV1 = ConfirmPageC(self.driver)
        #ConfirmPageV1.ConfirmPageFun1().click()
        ConfirmPageV.ConfirmPageFun1().click()
        #self.driver.find_element_by_link_text("Indonesia").click()

        #ConfirmPageV2 = ConfirmPageC(self.driver)
        #ConfirmPageV2.ConfirmPageFun2().click()
        ConfirmPageV.ConfirmPageFun2().click()
        #self.driver.find_element_by_class_name("checkbox-primary").click()

        #ConfirmPageV3 = ConfirmPageC(self.driver)
        #ConfirmPageV3.ConfirmPageFun3().click()
        ConfirmPageV.ConfirmPageFun3().click()
        #print(driver.find_element_by_css_selector(".alert-success").text)

        #ConfirmPageV4 = ConfirmPageC(self.driver)
        #success = ConfirmPageV4.ConfirmPageFun4().text
        success = ConfirmPageV.ConfirmPageFun4().text
        #success = self.driver.find_element_by_css_selector(".alert-success").text

        assert "Success! Thank you!" in success
        self.driver.get_screenshot_as_file("screenshot2.png")





