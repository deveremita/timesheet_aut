# Exibe uma mensagem de alerta informando que o script está rodando
Add-Type -AssemblyName 'System.Windows.Forms'
[System.Windows.Forms.MessageBox]::Show("Script em funcionamento!", "Alerta", "OK", "Information")

# Aguarda até que seja 21h
while ((Get-Date).Hour -ne 11) {
    Start-Sleep -Hours 1 
}

# Agora é 21h, exibe o popup perguntando se deseja rodar a automação do timesheet
$result = [System.Windows.Forms.MessageBox]::Show("Deseja rodar o Timesheet Automatizado hoje?", "Alerta", "YesNo", "Question")

# Verifica a resposta do usuário
if ($result -eq "Yes") {
    # Caminho do executável
    $exePath = "$env:UserProfile\Desktop\Timesheet Automatizado.lnk"
    # Executa o executável da automação do timesheet
    Start-Process -FilePath $exePath
}
# Encerra o script
Exit