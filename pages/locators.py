from selenium.webdriver.common.by import By


class YandexPageLocators():
    input_field = (By.CLASS_NAME, "input__control.input__input.mini-suggest__input")

    link_of_the_fist_site_on_the_result_page = (By.XPATH,
                                         "(//a[contains(@class, 'link')][contains(@class, 'link_theme_outer')]/b)[1]")

    link_to_pictures = (By.XPATH, "//div[contains(text(), 'Картинки')]")
    link_to_first_picture = (By.XPATH, "(//div[contains (@class, 'PopularRequestList-Shadow')])[1]")
    link_to_second_picture = (By.XPATH, "(//a[contains (@class, 'serp-item__link')])[2]")

    picture_switcher_right = (By.XPATH, "(//i[contains (@class, 'CircleButton-Icon')])[4]")
    picture_switcher_left = (By.XPATH, "(//i[contains (@class, 'CircleButton-Icon')])[1]")

    unique_picture_identifier = 'MMImage-Origin'


