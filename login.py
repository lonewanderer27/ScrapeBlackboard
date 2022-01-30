from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Login:

    def __init__(self):
        self.b = webdriver.Chrome('./chromedriver')
        self.b.maximize_window()

    def bb_login(self, user_id, password):
        self.b.get("https://adamson.blackboard.com/ultra/stream")
        print("blackboard opened")
        print("scrape start")

        # Select the agree button
        self.b.find_element_by_id("agree_button").send_keys(Keys.RETURN)
        print("clicked agree button")

        # Enter username
        self.b.find_element_by_id("user_id").send_keys(user_id)
        print("entered username, ")

        # Enter password
        self.b.find_element_by_id("password").send_keys(password)
        print("entered password")

        # Click Sign In
        print("signing in...")
        self.b.find_element_by_id("entry-login").send_keys(Keys.RETURN)
        print("success!")
