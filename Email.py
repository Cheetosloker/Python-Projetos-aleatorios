import pyautogui
import time
import pandas as pd
import pyperclip


# abridge o chrome e acessar a pagina
pyautogui.PAUSE = 1
pyautogui.hotkey("win")
pyautogui.write("chrome")
pyautogui.press("Enter")
time.sleep(3)
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("Enter")
time.sleep(3)

# login, senha e clicar em acessar
pyautogui.click(x=660, y=345)
pyautogui.write("Meu_login")
pyautogui.click(x=660, y=415)
pyautogui.write("Minha_senha")
pyautogui.click(x=660, y=495)
time.sleep(5)

# exportando a base
pyautogui.rightClick(x=350, y=263)
pyautogui.click(x=472, y=675)
time.sleep(3)

# calcular os indicadores
tabela = pd.read_csv(r"C:\Users\Administrador\Downloads\Compras.csv", sep=";")
total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco = total_gasto / quantidade
time.sleep(10)

# Enviar o email
pyautogui.hotkey("win")
pyautogui.write("chrome")
pyautogui.press("Enter")
time.sleep(3)
pyautogui.write("https://mail.google.com/mail/u/0/?tab=rm&ogbl")
pyautogui.press("Enter")
time.sleep(10)
pyautogui.click(x=71, y=159)
pyautogui.click(x=867, y=334)
pyautogui.write("mayconbarboza20@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "V")
pyautogui.press("tab")

texto = f"""
Prezados,

Segue relatório de compras
Total Gasto = R${total_gasto:,.2f}
Quantidade = {quantidade:}
Preco medio = R${preco:,.2f}

att.
"""
pyautogui.write(texto)
pyautogui.hotkey("ctrl", "enter")
# print(pyautogui.position())
