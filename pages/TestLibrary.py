import random
import re
import time

import requests
import xml.etree.ElementTree as et
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as Expected_Conditions
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class TestLibrary(BasePage):

    #WebElements
    sign_in_button = "//button[@class='btn btn-sm']"
    username_text_field = "inputUsername"
    password_text_field = "inputPassword"
    popup_sign_in = "//button[@class='btn btn-primary']"
    drop_down_list = "//button[@class='btn btn-sm dropdown-toggle']"
    collection = "//a[@href='/collection/user/cQGzkwoNyM']"
    table_id = "collectionitems"
    rows = "collection_objectname"
    column = "collection_title"
    game_titles = "//tbody/tr/td[contains(@id,'CEcell_objectname')]/div/a"
    language_dependence_info = "//span[@item-poll-button='languagedependence']/span"

    def check_if_home_page_is_open(self):
        assert self.driver.current_url == "https://boardgamegeek.com/"

    def click_on_sing_in_button(self):
        self.driver.find_element_by_xpath(self.sign_in_button).click()

    def log_user(self, user_id, password):
        self.driver.find_element_by_id(self.username_text_field).send_keys(user_id)
        self.driver.find_element_by_id(self.password_text_field).send_keys(password)
        self.driver.find_element_by_xpath(self.popup_sign_in).click()

    def go_to_user_collection(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.drop_down_list).click()
        self.driver.find_element_by_xpath(self.collection).click()

    def click_on_random_game_name(self):

        game_elements = wait(self.driver, 5).until(Expected_Conditions.visibility_of_all_elements_located((By.XPATH, self.game_titles)))
        game_elements[random.randrange(len(game_elements) - 1)].click()

    def get_current_url(self):
        return self.driver.current_url

    def request_builder(self):
        game_id = re.findall(r'\d+', self.get_current_url())[0]
        url = "http://www.boardgamegeek.com/xmlapi/boardgame/" + game_id

        headers = {
            'User-Agent': "PostmanRuntime/7.15.2",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "82b1a82c-7758-40d7-a5ad-03d11703bbef,8fc8e64b-dbf7-4d12-b50b-9657df004de7",
            'Host': "www.boardgamegeek.com",
            'Accept-Encoding': "gzip, deflate",
            'Referer': "http://www.boardgamegeek.com/xmlapi/boardgame/86174",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers)
        return str(response.text)

    def get_request_tree(self):
        return et.ElementTree(et.fromstring(self.request_builder()))

    def get_max_votes(self):
        tree = self.get_request_tree()
        language_dependency = tree.findall('.//poll[@name="language_dependence"]/results/result')
        max_votes = 0
        for element in range(len(language_dependency)):
            current_votes = int(language_dependency[element].get('numvotes'))
            if current_votes > max_votes:
                max_votes = current_votes
        return max_votes

    def assert_language_dependence_info(self):
        tree = self.get_request_tree()
        if self.get_max_votes() == 0:
            assert self.driver.find_element_by_xpath(self.language_dependence_info).text == "(no votes)"
        else:
            assert self.driver.find_element_by_xpath(self.language_dependence_info).text == tree.findall(
                './/poll[@name="language_dependence"]/results/result[@numvotes="' + str(self.get_max_votes()) + '"]')[0].get(
                'value') == self.driver.find_element_by_xpath(self.language_dependence_info).text
