from selenium.webdriver.common.by import By


class PedidosPageLocators:

    TEXT_NAME_PRODUCT_1 = (By.XPATH, '//*[@id="product_1_1_0_0"]/td[2]/p/a')
    TEXT_COMPRA_TOTAL = (By.ID, 'total_price')
    BUTTON_PROCEEED_TO_CHECKOUT = (By.XPATH, '//*[@id="center_column"]/p[2]/a[1]')

