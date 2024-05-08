from page_objects.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.Extract_infos_from_date import extrair_mes_ano

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
 
    def selecionar_o_mes_para_realizar_lancamento(self):
        nome_mes_e_ano_vigente = extrair_mes_ano()[0]

        # Elementos
        month_selection_area = (By.XPATH, '//*[@role="gridcell"]/..//*[@data-automationid="DetailsRowCell"]/..//*[contains(text(),"'+nome_mes_e_ano_vigente+'")]')
        launch_button = (By.XPATH, "//*[contains(text(),'Lançamentos')]")
        #Ações
        self.find_and_click(month_selection_area)
        self.find_and_click(launch_button)