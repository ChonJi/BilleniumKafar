from driversetup.DriverSetup import DriverSetup

from pages.TestLibrary import TestLibrary


class TestLoginPage(DriverSetup):

    user_id = "cQGzkwoNyM"
    user_password = "forthehorde"

    def test_should_go_to_login_page_and_log_in(self):
        test_library = TestLibrary(self.driver)
        test_library.check_if_home_page_is_open()
        test_library.click_on_sing_in_button()
        test_library.log_user(self.user_id, self.user_password)
        test_library.go_to_user_collection()
        test_library.click_on_random_game_name()
        test_library.request_builder()
        test_library.assert_language_dependence_info()




