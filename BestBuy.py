import base64
import os
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# Desired capabilities for Appium
desired_cap = {
    "platformName": "Android Automation",
    "platformVersion": "10.0",
    "appPackage": "com.coppi.bestbuy",
    "appActivity": "com.bestbuy.android.activity.HomeScreenActivity",
    "newCommandTimeout": 600,
}

# Initialize the Appium driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

# Start recording the screen
driver.start_recording_screen()
time.sleep(8)

# Navigate through the app using XPath
driver.find_element_by_xpath("//android.widget.TextView[@text='Products']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='Computers, Tablets & Accessories']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='Laptops and Desktops']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='MacBooks']").click()
driver.implicitly_wait(5)

# Perform touch actions for scrolling
TouchAction(driver).long_press(x=322, y=1109).move_to(x=327, y=410).release().perform()

for i in range(1):
    touch = TouchAction(driver)
    touch.long_press(x=322, y=1109).move_to(x=327, y=410).release().perform()
    time.sleep(2)

# Perform gestures like tapping and long pressing
gestures = TouchAction(driver)
gestures.tap(x=357, y=108).perform()
gestures.long_press(x=333, y=1050).move_to(x=357, y=239).release().perform()
gestures.long_press(x=326, y=242).move_to(x=343, y=1050).release().perform()

# Search for a specific product
driver.find_element_by_id("com.coppi.bestbuy:id/toolbarSearchHint").click()
driver.find_element_by_id("com.coppi.bestbuy:id/search_edit_text").send_keys("SONY 1000XM4")
gestures.tap(x=656, y=1305).perform()

# Navigate to gaming laptops section
driver.implicitly_wait(5)
gestures.tap(x=350, y=98).perform()
driver.find_element_by_xpath("//android.widget.TextView[@text='Products']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='Laptops']").click()
driver.implicitly_wait(5)
driver.find_element_by_id("com.coppi.bestbuy:id/sortAndFilter").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("(//android.widget.TextView[@content-desc='bestBuySortFilterExpandFacet'])[1]").click()
driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Gaming Laptops (1637)']").click()
time.sleep(4)
driver.find_element_by_id("com.coppi.bestbuy:id/apply").click()
time.sleep(4)

# Perform gestures for scrolling after applying the filter
gestures.long_press(x=316, y=1203).move_to(x=343, y=398).release().perform()
driver.implicitly_wait(5)
gestures.long_press(x=316, y=1203).move_to(x=343, y=398).release().perform()
driver.implicitly_wait(5)
gestures.long_press(x=333, y=444).move_to(x=324, y=1118).release().perform()
driver.implicitly_wait(15)
time.sleep(4)
gestures.tap(x=118, y=458).perform()

# Add a product to the cart and view the cart
gestures.long_press(x=316, y=1203).move_to(x=343, y=398).release().perform()
driver.implicitly_wait(5)
gestures.long_press(x=316, y=1203).move_to(x=343, y=398).release().perform()
driver.implicitly_wait(5)
time.sleep(4)
gestures.long_press(x=333, y=444).move_to(x=324, y=1118).release().perform()
driver.find_element_by_xpath("//android.widget.TextView[@text='Add To Cart']").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='View Cart']").click()
time.sleep(7)
gestures.long_press(x=316, y=1203).move_to(x=343, y=398).release().perform()
driver.implicitly_wait(5)
gestures.long_press(x=316, y=1203).move_to(x=343, y=398).release().perform()
driver.implicitly_wait(5
