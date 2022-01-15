from selenium import webdriver
import time

browser = webdriver.Chrome("C:\sel\chromedriver.exe")

browser.get("http://twitter.com/login")
browser.find_element_by_class_name("js-username-field").send_keys("expectoopatronm")
browser.find_element_by_class_name("js-password-field").send_keys("password")
browser.find_element_by_class_name("clearfix").submit()
browser.get("http://twitter.com/expectoopatronm")

menu = browser.find_elements_by_class_name("my-tweet")

twitNumber = len(menu)

for a in range(twitNumber):


    browser.find_element_by_class_name("ProfileTweet-actionButton").click()
    browser.find_element_by_xpath("//*[contains(text(), 'Tweeti sil')]").click()
    browser.find_element_by_class_name("delete-action").click()

    time.sleep(2)
