import unittest
from selenium import webdriver


class DriverSetup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://boardgamegeek.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
