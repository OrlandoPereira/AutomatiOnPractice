from selenium.webdriver.common.by import By


class EnderecoDeEntregaPageLocators:
    """YOUR DELIVERY ADDRESS"""
    TEXT_ADDRESS = (By.XPATH, '//*[@id="address_delivery"]/li[3]')
    TEXT_CITY_STATE_POSTCODE = (By.XPATH, '//*[@id="address_delivery"]/li[4]')
    TEXT_YOUR_DELIVERY_ADDRESS = (By.XPATH, '//*[@id="address_delivery"]/li[1]/h3')

    ''''''
    BUTTON_PROCEED_TO_CHECKOUT = (By.NAME, 'processAddress')
