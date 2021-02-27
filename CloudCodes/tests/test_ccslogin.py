

import pytest
import unittest
from PageObject.LoginPageCCS import LoginPageCCS1
from utilities.BaseClass import BaseClass1

class CCSLogin(BaseClass1,unittest.TestCase):

    def test_ccslogin(self):

        LoginPageCCS1V = LoginPageCCS1(self.driver)
        LoginPageCCS1V.get_loginname().send_keys("appsadmin@cloudcodesqa5.in")
        LoginPageCCS1V.checkbtn().click()
        LoginPageCCS1V.password1().send_keys("appspass")
        LoginPageCCS1V.getpassword1().click()
        LoginPageCCS1V.announceid().click()
        #self.driver.find_element_by_id("login-name").send_keys("appsadmin@isb.gappspilot.info")
        #self.driver.find_element_by_class_name("signinbtn").click()
        #self.driver.find_element_by_name("password").send_keys(getData[1])
        #self.driver.find_element_by_xpath("//input[@type='submit']").click()
        #self.driver.find_element_by_id("announcemntFooterbtn").click()
        #self.driver.find_element_by_class_name("text-center").click()
        #childwindow = self.driver.window_handles[1]
        #self.driver.switch_to.window(childwindow)
        #self.driver.maximize_window()

    #@pytest.fixture(params=[("appsadmin@cloudcodesqa5.in", "appspass"),("nias@cloudcodesqa5.in", "appspass")])
    #def getData(self, request):
     #   return request.param
unittest.main()