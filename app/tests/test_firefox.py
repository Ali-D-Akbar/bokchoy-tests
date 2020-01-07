import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome = webdriver.Remote(
          command_executor='http://selenium-hub:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)
firefox = webdriver.Remote(
          command_executor='http://selenium-hub:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.FIREFOX)

chrome.get('http://demo.app:8000/polls/')
print(chrome.title)

firefox.get('http://demo.app:8000/polls/')
print(firefox.title)

chrome.quit()
firefox.quit()
