from page_objects.base import BasePage
from page_objects.size_page import SizePage
from page_objects.each_size_page import EachSizePage


class TestBaseScenarios():

    def test_tire_availability(self, driver):
        base = BasePage(driver)
        size_page = SizePage(driver)
        each_size_page = EachSizePage(driver)
        size_page.open()
        radius_buttons_links = size_page.get_radius_buttons_links()
        each_size_buttons_links = each_size_page.get_size_buttons_links(radius_buttons_links)
        tire_data = each_size_page.get_tire_data(each_size_buttons_links)
        base.csv_file_creator(tire_data)
        driver.close()
