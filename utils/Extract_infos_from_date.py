import time 
def extrair_mes_ano():
    # Lista com os nomes dos meses
    meses_do_ano = ["Janeiro", "Fevereiro", "Março", "Abril", 
        "Maio", "Junho", "Julho", "Agosto", 
        "Setembro", "Outubro", "Novembro", "Dezembro"]

    # Obter o tempo atual em segundos
    tempo_atual = time.time()

    # Converter o tempo atual em uma tupla com as informações locais
    info_tempo_local = time.localtime(tempo_atual)

    #Extrair o mês da tupla
    mes_vigente = info_tempo_local.tm_mon
    #Extrair o ano da tupla
    ano_vigente = info_tempo_local.tm_year
    #Obter o nome do mês correspondente
    nome_mes_vigente = meses_do_ano[mes_vigente -1]
    
    nome_mes_e_ano_vigente = f'{nome_mes_vigente.lower()} {ano_vigente}'
    return nome_mes_e_ano_vigente, nome_mes_vigente, ano_vigente

    
    
def extrair_data_completa():
    _,nome_mes_vigente, ano_vigente = extrair_mes_ano()
    #mes_e_ano_vigente, nome_mes_vigente, ano_vigente = extrair_mes_ano()
    #Extrair o dia da tupla
    dia_vigente = time.localtime().tm_mday
    
    return f'{nome_mes_vigente.capitalize()} {dia_vigente}, {ano_vigente}'
        
        

    

    
