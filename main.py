import unittest
from selenium import webdriver
import page
import time

class CasaPariurilor(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.superbet.ro")
        self.driver.maximize_window()

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

    def test_search_pariuri(self):
        mainPage = page.MainPage(self.driver)
        time.sleep(4)
        mainPage.go_to_home_page()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        time.sleep(4)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_not_found()

    def test_click_link_superoferta(self):
        link = page.ClickingLink(self.driver, "JOCURI")
        link.click_text()

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
