from selenium.webdriver.common.by import By


class PagamentoPageLocators:

    TEXT_COMPRA_TOTAL = (By.ID, 'total_price')
    TEXT_YOUR_ORDER_ON_MY_STORE_IS_COMPLETE = (By.XPATH, '//*[@id="center_column"]/div/p/strong')
    BUTTON_PAY_BY_BANK_WIRE = (By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')
    BUTTON_I_CONFIRM_MY_ORDER = (By.XPATH, '//*[@id="cart_navigation"]/button')

