import pyautogui  ## Controla o mouse, teclado e tela no seu computador
import time

# pyautogui.click -> Clicar com o mouse
# pyautogui.write -> Escrever um texto
# pyautogui.press -> Apertar uma tecla
# pyautogui.hotkey -> Apertar um atalho - uma combinação de teclas

pyautogui.PAUSE = (1) ##Para todos os comandos, iNSIRA SUA SENHA executar, com 1 segundo de intervalo

# Passo 1: Acessar a tela de login do GitHub

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://github.com/login")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=843, y=357)
pyautogui.write("Login")
pyautogui.click(x=851, y=454)
pyautogui.write("Senha")
