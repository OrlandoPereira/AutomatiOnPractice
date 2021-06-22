from selenium.webdriver.common.by import By


class ProdutoPageLocators:

    BUTTON_ADD_TO_CART = (By.XPATH, '//*[@id="add_to_cart"]/button/span')
    BUTTON_PROCEEED_TO_CHECKOUT = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')
    TEXT_NAME_PRODUCT = (By.XPATH, '//*[@id="center_column"]/div/div/div[3]/h1')

