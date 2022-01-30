from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Courses:

    def __init__(self, login):
        self.b = login

    def courses_view(self):
        time.sleep(4)
        # Navigate to Courses page
        self.b.find_element_by_xpath('//*[@id="base_tools"]/bb-base-navigation-button[4]').click()
        print("clicked courses")

        time.sleep(3)
        # Press the Courses drop-down
        self.b.find_element_by_xpath('//*[@id="active-term-name"]').click()
        print("clicked courses drop-down menu")
        # Choose second sem category
        self.b.find_element_by_xpath('//*[@id="courses-terms"]/li[3]/a/span').click()
        print("chose 2nd Sem category")

        time.sleep(3)
        # Returns courses
        return self.b.find_elements_by_class_name("js-course-title-element")
