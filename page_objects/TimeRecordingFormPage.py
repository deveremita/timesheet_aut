from page_objects.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.Extract_infos_from_date import extrair_data_completa

class TimeRecordingFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def preencher_o_form_e_salvar(self):
        data_completa = extrair_data_completa()
        # Elementos mapeados e ações para Novos Lançamentos - Formulário de preenchimento
        date_select_box = (By.XPATH, '//*[@aria-label="Selecione uma data"]')
        day_item = (By.XPATH, '//*[@aria-label="'+data_completa+'"]')
        start_time = (By.XPATH, '//*[@name="horaInicial"]') 
        end_time = (By.XPATH, '//*[@name="horaFinal"]')
        lunchtime = (By.XPATH, '//*[@name="horaAlmoco"]')
        project_select_box = (By.XPATH,'(//*[@role="listbox"])[2]')
        task_select_box = (By.XPATH,'(//*[@role="listbox"])[3]')
        save_button = (By.XPATH,'//*[button]/..//*[contains(text(),"Salvar")]')

        self.find_and_click(date_select_box)
        self.find_and_click(day_item)
        self.find_and_send_keys(start_time, "AM", Keys.ARROW_LEFT, Keys.ARROW_LEFT, "0900")
        self.find_and_send_keys(end_time, "PM", Keys.ARROW_LEFT, Keys.ARROW_LEFT, "0600")
        self.find_and_send_keys(lunchtime, "AM", Keys.ARROW_LEFT, Keys.ARROW_LEFT, "0100")
        self.find_and_send_keys(project_select_box,Keys.TAB)
        self.find_and_send_keys(task_select_box,Keys.TAB)
        self.find_and_click(save_button)
        #endregion