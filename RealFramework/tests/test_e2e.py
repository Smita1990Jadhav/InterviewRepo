import time

from Tools.scripts.fixcid import String
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome(executable_path="C:\\pythondrivers\chromedriver.exe")
#driver.implicitly_wait(20)
driver.get("https://www.amazon.in")
#time.sleep(5)
driver.maximize_window()
#get_title = driver.title
print(driver.title)
"""
driver.find_element_by_id("nav-hamburger-menu").click()
time.sleep(5)
driver.find_element_by_xpath("//div[@id='hmenu-content']/ul/li[29]").click()
driver.find_element_by_id("ap_email").send_keys("919168840203")
driver.find_element_by_id("continue").click()
driver.find_element_by_id("ap_password").send_keys("Smita@123")
driver.find_element_by_id("signInSubmit").click()
"""
driver.find_element_by_id("twotabsearchtextbox").send_keys("w")
time.sleep(4)
products = driver.find_elements_by_css_selector("div[class='s-suggestion'] span")
print(len(products))

for product in products:
    print(product.text)
    if product.text=="atch for man":
        product.click()
        break
time.sleep(2)
#wait = WebDriverWait(driver, 10)
#wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Analog Grey Dial Men's Watch-MTP-V006L-3BUDF (A1767)"))).click()
driver.find_element_by_css_selector("img[data-image-index='3']").click()
#driver.execute_script("window-scrollTo(0,document.body.scrollHeight);")
#if ele.is_displayed():
#   ele.click()
#else:
#driver.find_element_by_class_name("a-last").click()

#time.sleep(2)
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)
obj = Select(driver.find_element_by_id("quantity"))
obj.select_by_value("2")
driver.find_element_by_css_selector("span[id='submit.add-to-cart']").click()
driver.find_element_by_css_selector("div[id='nav-cart-count-container']").click()
driver.find_element_by_css_selector("input[type='checkbox']").click()
driver.find_element_by_css_selector("span[class='a-button-inner'] input").click()
time.sleep(2)
driver.find_element_by_id("ap_email").send_keys("919168840203")
driver.find_element_by_id("continue").click()
driver.find_element_by_id("ap_password").send_keys("Manoj@123")
driver.find_element_by_id("signInSubmit").click()
time.sleep(15)
#print(driver.find_element_by_css_selector("div[class='displayAddressDiv']").text)
#assert "Mauli Building, Behind Bus Stand" in address
driver.get_screenshot_as_file("screenshots.png")




