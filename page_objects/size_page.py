from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base import BasePage


class SizePage(BasePage):
    __size_page_url = 'https://www.bridgestonetire.com/size/'
    __radius_buttons_locator = (By.XPATH, "//div[@class='cmp-in-page-nav']//div[@class='button']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__size_page_url)

    def get_radius_buttons_links(self) -> list:
        return super()._get_links_from_elements(self.__radius_buttons_locator)
