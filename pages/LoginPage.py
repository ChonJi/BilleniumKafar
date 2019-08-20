import random
import re
import time

import requests
import xml.etree.ElementTree as et

from pages.BasePage import BasePage


class LoginPage(BasePage):

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



    """
    driver.get(base_url)
    driver.find_element_by_xpath(base_sign_in).click()
    driver.find_element_by_id(text_field_username).send_keys(Credentials.username)
    driver.find_element_by_id(text_field_password).send_keys(Credentials.password)
    driver.find_element_by_xpath(popup_sign_in).click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(dropdown_list).click()
    driver.find_element_by_xpath(collection)

    """

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
        time.sleep(2)
        game_elements = self.driver.find_elements_by_xpath(self.game_titles)
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

    def assert_language_dependencies_text(self):
        tree = et.ElementTree(et.fromstring(self.request_builder()))
        language_dependency = tree.findall('//poll[@name="language_dependence"]/results/result')
        for element in range(len(language_dependency)):
            print(language_dependency[element].get('value'))
            print(language_dependency[element].get('numvotes'))





