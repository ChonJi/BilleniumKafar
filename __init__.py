from selenium import webdriver


class home_page:

    driver = webdriver.Chrome()

    sign_in_button = "btn btn-sm"

    def sign_in(self):

        self.driver.find_element_by_class_name(self.sign_in_button).click()




