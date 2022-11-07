from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import csv


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_elements(self, elements_locator):
        elements_list = self._driver.find_elements(*elements_locator)
        return elements_list

    def _get_links_from_elements(self, locator):
        return [link.find_element(By.CSS_SELECTOR, "a").get_attribute('href') for link in self._get_elements(locator)]

    def _list_append_variable_arguments(self, *arg):
        return [*arg]

    def csv_file_creator(self, data):
        with open('tire_data.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(
                data
            )