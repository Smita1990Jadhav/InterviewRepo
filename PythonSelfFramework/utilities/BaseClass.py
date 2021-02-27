import inspect
import logging

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass1:
    def test_loggingDemo2(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        FileHandlerC = logging.FileHandler('logfilesm1.log')
        FormatterC = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        FileHandlerC.setFormatter(FormatterC)
        logger.addHandler(FileHandlerC)
        logger.setLevel(logging.INFO)
        return logger
    def VerifyText(self, text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
    def SelectOptByText(self,locator,text):
        obj = Select(locator)
        obj.select_by_visible_text(text)