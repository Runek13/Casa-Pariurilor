from selenium.webdriver.common.by import By


class MainPageLocators(object):
    GO_BUTTON = (By.CLASS_NAME, "verification-bar__button")
    HOME_PAGE_BUTTON = (By.ID, "sb-logo")
    MODAL = (By.CLASS_NAME, "modal__container")
    TITLE = (By.CLASS_NAME, "modal__title")

class SearchResultsPageLocators(object):
    pass