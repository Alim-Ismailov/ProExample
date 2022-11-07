from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from bs4 import BeautifulSoup
import requests
from page_objects.base import BasePage


class EachSizePage(BasePage):
    __size_buttons_locator = (By.XPATH, "//ul[@class='tires-by-diameter__links']/li")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_size_buttons_links(self, links: list):
        size_buttons_links = []
        for link in links:
            super()._open_url(link)
            size_buttons_links += (super()._get_links_from_elements(self.__size_buttons_locator))
        return size_buttons_links

    def get_tire_data(self, urls):
        tire_data = [['TireSize', 'TireCount', 'URL']]
        for url in urls:
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text, 'lxml')
            ad = soup.find_all('div', class_='cmp-tire-card cmp-tire-card-search')
            tire_count = len(ad)
            tire_size = ((url.split('/'))[-2]).replace('r', 'R').replace('-', '/')
            tire_data.append(super()._list_append_variable_arguments(tire_size, tire_count, url))
        return tire_data
