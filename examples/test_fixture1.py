from selenium import webdriver
import pytest

link = "http://selenium1py.pythonanywhere.com/"



@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")




class TestMainPage1():

    # @classmethod
    # def setup_class(self):
    #     print("\nstart browser for test suite..")
    #     self.browser = webdriver.Chrome()

    # @classmethod
    # def teardown_class(self):
    #     print("quit browser for test suite..")
    #     browser.quit()

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.skip
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")


# class TestMainPage2():
#
#     def setup_method(self):
#         print("start browser for test..")
#         self.browser = webdriver.Chrome()
#
#     def teardown_method(self):
#         print("quit browser for test..")
#         self.browser.quit()
#
#     def test_guest_should_see_login_link(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")