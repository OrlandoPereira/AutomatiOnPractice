from selenium.webdriver.common.by import By


class EnvioPageLocators:

    CHECK_TERMS_OF_SERVICE = (By.XPATH, '//*[@id="cgv"]')
    BUTTON_PROCEEED_TO_CHECKOUT = (By.XPATH, '//*[@id="form"]/p/button')

