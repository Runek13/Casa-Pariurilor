from locator import *
from element import BasePageElement


class SearchTextElement(BasePageElement):
    locator = "tickedId"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):


    search_text_element = SearchTextElement

    def is_title_matches(self):
        return "Superbet | Pariuri Sportive Online, Live, Casino, Loto, Virtuale" in self.driver.title

    def go_to_home_page(self):
        element = self.driver.find_element(*MainPageLocators.HOME_PAGE_BUTTON)
        element.click()

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultPage(BasePage):

     def is_results_not_found(self):
         self.driver.find_element(*MainPageLocators.MODAL)
         element_title = self.driver.find_element(*MainPageLocators.TITLE)
         return "BILETUL NU A FOST GĂSIT" == element_title.text


class ClickingLink(BasePage):

    def __init__(self, driver, text):
        super().__init__(driver)
        self.text = text

    def click_text(self):
        link = self.driver.find_element_by_link_text(self.text)
        link.click()

