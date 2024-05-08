from page_objects.BasePage import BasePage
from utils.Config import LOGIN_PASS,LOGIN_USER
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def logar_no_sharepoint(self):
        # Elementos
        username_input = (By.NAME,'loginfmt')
        button = (By.ID,'idSIButton9')
        pass_input = (By.NAME,'passwd')
        # Ações
        self.find_and_send_keys(username_input, LOGIN_USER)
        self.find_and_click(button)
        self.find_and_send_keys(pass_input, LOGIN_PASS)
        self.find_and_click(button)

        try:
            while EC.presence_of_element_located(button):
                self.find_and_click(button)
        except TimeoutException:
            print("OK")
