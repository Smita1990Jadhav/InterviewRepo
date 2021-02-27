#https://docs.pytest.org/_/downloads/en/2.8.7/pdf/
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from PageObject.HomePage import HomePageC
from TestData import HomePagedata
from TestData.HomePagedata import HomePageData
from utilities.BaseClass import BaseClass1


class TestHomePage(BaseClass1):

    def test_formsubmission(self,getData):
        log = self.test_loggingDemo2()
        HomepageV = HomePageC(self.driver)
        log.info("First name is"+getData["firstname"])
        HomepageV.getname().send_keys(getData["firstname"])
        #driver.find_element_by_name("name").send_keys("Smita")

        #driver.find_element_by_name("email").send_keys("jadhavpiya1990@gmail.com")
        HomepageV.getemail().send_keys(getData["lastname"])
        #driver.find_element_by_id("exampleInputPassword1").send_keys("Piya@123")
        HomepageV.getpassword().send_keys(getData["gender"])
        #driver.find_element_by_id("exampleCheck1").click()
        HomepageV.checkboxopt().click()
        # time.sleep(10)
        # obj = Select(driver.find_element_by_id("//div[@class='form-group']/select/option"))
        """
        Below Code can be reusable so it is added in BaseClass(utilities)
        obj = Select(HomepageV.dropdn())
        obj.select_by_visible_text("Female")
        """
        self.SelectOptByText(HomepageV.dropdn(), "Female")
        #driver.find_element_by_id("inlineRadio2").click()
        HomepageV.radiobopt().click()
        #driver.find_element_by_xpath("//input[@value='Submit']").click()
        HomepageV.submitb().click()
        #AlertText = driver.find_element_by_css_selector("[class*='alert-success']").text
        AlertText = HomepageV.successmsgfun().text

        assert ("success" in AlertText)

    """
    @pytest.fixture(params=[("Smita","Jadhav","Female"),("Vivaan","Sharma","Male")])
    def getData(self, request):
        return request.param
    """
    #Below code for how to use Dictionary
    @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    def getData(self, request):
        return request.param

