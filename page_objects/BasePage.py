from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.ac = ActionChains(self.driver)
           
    #region Métodos tratados com expected_conditions para click, e send_keys
    def find_and_send_keys(self, locator, *keys):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.ac.move_to_element(element).click().send_keys(*keys).perform()

    def find_and_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.ac.move_to_element(element).click().perform()
    #endregion