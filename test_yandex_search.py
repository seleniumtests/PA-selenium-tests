from pages.yandex_search_page import YandexSearchPage
from pages.locators import YandexPageLocators


def test_open_perfect_art_site(browser):
    link = "https://yandex.ru/"
    phrase = 'perfect art'

    page = YandexSearchPage(browser, link)
    page.open()
    page.search_phrase(phrase)
    page.select_line_from_suggested_search_list(0)
    assert page.get_name_of_the_first_link_on_the_results_page() == "perfectart.ru", \
        "Первая ссылка не введет на perfectart.ru"

    page.open_and_switch_to_new_tab(YandexPageLocators.link_of_the_fist_site_on_the_result_page)
    assert page.get_new_url() == "https://perfectart.ru/", "Открылся не сайт https://perfectart.ru/"


def test_open_pictures(browser):
    link = "https://yandex.ru/"

    page = YandexSearchPage(browser, link)
    page.open()

    page.open_and_switch_to_new_tab(YandexPageLocators.link_to_pictures)
    page.click_element(YandexPageLocators.link_to_first_picture)
    page.click_element(YandexPageLocators.link_to_second_picture)
    identifier_first_picture = page.get_unique_picture_identifier()

    page.click_element(YandexPageLocators.picture_switcher_right)
    identifier_second_picture = page.get_unique_picture_identifier()
    assert identifier_first_picture != identifier_second_picture, "Картинка не изменилась!"

    page.click_element(YandexPageLocators.picture_switcher_left)
    identifier_third_picture = page.get_unique_picture_identifier()
    assert identifier_first_picture == identifier_third_picture, "Картинка 1 не вернулась обратно!"
