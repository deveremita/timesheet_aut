from utils.Config import URL
from page_objects.LoginPage import *
from page_objects.MainPage import *
from page_objects.TimeRecordingFormPage import *
from selenium import webdriver


driver = webdriver.Firefox()
driver.get(URL)

login_page = LoginPage(driver)
main_page = MainPage(driver)
time_recording_form_page = TimeRecordingFormPage(driver)

login_page.logar_no_sharepoint()
main_page.selecionar_o_mes_para_realizar_lancamento()
time_recording_form_page.preencher_o_form_e_salvar()

