from selenium.webdriver.common.by import By


class CriarContaPageLocators:
    """YOUR PERSONAL INFORMATION"""
    CHECK_BUTTON_MR = (By.XPATH, '//*[@id="id_gender1"]')
    INPUT_TEXT_FIRST_NAME = (By.NAME, 'customer_firstname')
    INPUT_TEXT_LAST_NAME = (By.NAME, 'customer_lastname')
    INPUT_TEXT_EMAIL = (By.ID, 'email')
    INPUT_TEXT_PASSWORD = (By.ID, 'passwd')
    '''YOUR ADDRESS'''
    INPUT_TEXT_ADDRESS = (By.ID, 'address1')
    INPUT_TEXT_CITY = (By.ID, 'city')
    SELECT_TEXT_STATE = (By.ID, 'id_state')

    INPUT_TEXT_ZIP_POSTAL_CODE = (By.ID, 'postcode')
    # INPUT_TEXT_COUNTRY = (By.ID, '')
    ''''''
    INPUT_TEXT_MOBILE_PHONE = (By.ID, 'phone_mobile')
    INPUT_TEXT_ADDRESS_REFERENCE = (By.XPATH, '//*[@id="alias"]')
    ''''''
    BUTTON_REGISTER = (By.ID, 'submitAccount')



