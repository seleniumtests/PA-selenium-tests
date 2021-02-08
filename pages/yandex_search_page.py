from .base_page import BasePage
from .locators import YandexPageLocators


class YandexSearchPage(BasePage):
    def search_phrase(self, phrase):
        search_input_field = self.browser.find_element(*YandexPageLocators.input_field)
        search_input_field.send_keys(phrase)

    def select_line_from_suggested_search_list(self, index):
        select = self.browser.find_element_by_css_selector(f"[data-index = '{index}']")
        select.click()

    def get_name_of_the_first_link_on_the_results_page(self):
        link = self.browser.find_element(*YandexPageLocators.link_of_the_fist_site_on_the_result_page)
        link_text = link.text
        return link_text

    def open_and_switch_to_new_tab(self, locator):
        link = self.browser.find_element(*locator)
        link.click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def click_element(self, locator2):
        link = self.browser.find_element(*locator2)
        link.click()

    def get_new_url(self):
        return self.browser.current_url

    def get_unique_picture_identifier(self):
        link = self.browser.find_element_by_class_name(YandexPageLocators.unique_picture_identifier)
        src = link.get_attribute('src')
        return src
