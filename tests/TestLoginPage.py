from driversetup.DriverSetup import DriverSetup
from pages.LoginPage import LoginPage


class TestLoginPage(DriverSetup):

    user_id = "cQGzkwoNyM"
    user_password = "forthehorde"

    def test_should_go_to_login_page_and_log_in(self):
        login_page = LoginPage(self.driver)
        login_page.check_if_home_page_is_open()
        login_page.click_on_sing_in_button()
        login_page.log_user(self.user_id, self.user_password)
        login_page.go_to_user_collection()
        login_page.click_on_random_game_name()
        login_page.request_builder()
        login_page.get_max_votes()
        login_page.assert_language_dependence_info()




